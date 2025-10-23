#!/usr/bin/env python3
"""
track_portfolio.py - Save portfolio snapshots to database

Fetches current portfolio from Kraken API and saves it to the database
for historical tracking and performance analysis.

Usage:
    python3 track_portfolio.py                    # Save current portfolio
    python3 track_portfolio.py --history 30       # Show last 30 snapshots
    python3 track_portfolio.py --compare          # Compare to previous snapshot
    python3 track_portfolio.py --csv              # Export to CSV
"""

import sqlite3
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from fetch_portfolio import PortfolioFetcher

DB_PATH = Path(__file__).parent.parent / 'portfolio_tracker.db'


def save_portfolio_snapshot(portfolio_data):
    """Save portfolio snapshot to database"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        timestamp = datetime.utcnow().isoformat()
        total_value = portfolio_data.get('total_value_usd', 0)
        spot_value = portfolio_data.get('spot_value_usd', 0)
        earn_value = portfolio_data.get('earn_value_usd', 0)
        holdings_json = json.dumps(portfolio_data)
        
        # Insert portfolio snapshot
        cursor.execute('''
            INSERT INTO portfolio_snapshots 
            (timestamp, total_value_usd, spot_value_usd, earn_value_usd, holdings_json)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, total_value, spot_value, earn_value, holdings_json))
        
        snapshot_id = cursor.lastrowid
        
        # Insert spot portfolio holdings
        for holding in portfolio_data.get('spot_portfolio', []):
            cursor.execute('''
                INSERT INTO asset_holdings
                (snapshot_id, asset, amount, price_usd, value_usd, allocation_pct, source)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                snapshot_id,
                holding['asset'],
                holding['amount'],
                holding.get('price_usd', 0),
                holding['value_usd'],
                holding.get('weight', 0),
                'spot'
            ))
        
        # Insert earn allocations
        for allocation in portfolio_data.get('earn_allocations', []):
            cursor.execute('''
                INSERT INTO asset_holdings
                (snapshot_id, asset, amount, price_usd, value_usd, allocation_pct, source)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                snapshot_id,
                allocation['asset'],
                allocation['amount'],
                allocation.get('price_usd', 0),
                allocation['value_usd'],
                0,  # Will calculate from value
                'earn'
            ))
        
        conn.commit()
        conn.close()
        
        print(f"✓ Portfolio snapshot saved")
        print(f"  Timestamp: {timestamp}")
        print(f"  Total Value: ${total_value:.2f}")
        print(f"  Holdings: {len(portfolio_data.get('spot_portfolio', []))} spot + {len(portfolio_data.get('earn_allocations', []))} earn")
        
        return snapshot_id
        
    except Exception as e:
        print(f"✗ Error saving portfolio: {e}")
        return None


def show_history(days=30):
    """Show portfolio history"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cutoff_date = (datetime.utcnow() - timedelta(days=days)).isoformat()
        
        cursor.execute('''
            SELECT timestamp, total_value_usd, spot_value_usd, earn_value_usd
            FROM portfolio_snapshots
            WHERE timestamp > ?
            ORDER BY timestamp DESC
        ''', (cutoff_date,))
        
        rows = cursor.fetchall()
        
        print(f"\n📊 Portfolio History (Last {days} days)")
        print("=" * 80)
        print(f"{'Timestamp':<25} {'Total Value':<15} {'Spot':<15} {'Earn':<15}")
        print("-" * 80)
        
        for row in rows:
            timestamp, total, spot, earn = row
            # Parse ISO format timestamp
            dt = datetime.fromisoformat(timestamp)
            display_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            print(f"{display_time:<25} ${total:>12.2f}  ${spot:>12.2f}  ${earn:>12.2f}")
        
        if rows:
            # Calculate change
            latest = rows[0]
            oldest = rows[-1]
            change = latest[1] - oldest[1]
            change_pct = (change / oldest[1] * 100) if oldest[1] != 0 else 0
            
            print("-" * 80)
            print(f"Change: ${change:+.2f} ({change_pct:+.2f}%)")
        
        conn.close()
        
    except Exception as e:
        print(f"✗ Error fetching history: {e}")


def compare_to_previous():
    """Compare current portfolio to previous snapshot"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, timestamp, total_value_usd, holdings_json
            FROM portfolio_snapshots
            ORDER BY timestamp DESC
            LIMIT 2
        ''')
        
        rows = cursor.fetchall()
        
        if len(rows) < 2:
            print("⚠️  Not enough historical data for comparison")
            conn.close()
            return
        
        current = rows[0]
        previous = rows[1]
        
        current_value = current[2]
        previous_value = previous[2]
        change = current_value - previous_value
        change_pct = (change / previous_value * 100) if previous_value != 0 else 0
        
        print(f"\n📈 Portfolio Comparison")
        print("=" * 60)
        print(f"Current:  ${current_value:.2f}")
        print(f"Previous: ${previous_value:.2f}")
        print(f"Change:   ${change:+.2f} ({change_pct:+.2f}%)")
        print(f"Time:     {previous[1]} → {current[1]}")
        
        conn.close()
        
    except Exception as e:
        print(f"✗ Error comparing: {e}")


def export_csv(output_file=None):
    """Export portfolio history to CSV"""
    try:
        import csv
        
        if not output_file:
            output_file = Path.cwd() / 'portfolio_history.csv'
        
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT timestamp, total_value_usd, spot_value_usd, earn_value_usd
            FROM portfolio_snapshots
            ORDER BY timestamp
        ''')
        
        rows = cursor.fetchall()
        
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Total Value (USD)', 'Spot Value (USD)', 'Earn Value (USD)'])
            writer.writerows(rows)
        
        print(f"✓ Portfolio history exported to {output_file}")
        
        conn.close()
        
    except Exception as e:
        print(f"✗ Error exporting: {e}")


def main():
    if '--history' in sys.argv:
        # Show history
        idx = sys.argv.index('--history')
        days = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 30
        show_history(days)
        return 0
    
    elif '--compare' in sys.argv:
        # Compare to previous
        compare_to_previous()
        return 0
    
    elif '--csv' in sys.argv:
        # Export to CSV
        export_csv()
        return 0
    
    else:
        # Fetch and save current portfolio
        print("🔄 Fetching current portfolio from Kraken...")
        fetcher = PortfolioFetcher()
        portfolio = fetcher.get_portfolio_summary()
        
        if portfolio:
            snapshot_id = save_portfolio_snapshot(portfolio)
            if snapshot_id:
                print(f"\n✅ Portfolio tracking updated (ID: {snapshot_id})")
                return 0
        
        print("✗ Failed to fetch or save portfolio")
        return 1


if __name__ == '__main__':
    sys.exit(main())
