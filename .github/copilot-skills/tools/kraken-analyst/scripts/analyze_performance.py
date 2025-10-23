#!/usr/bin/env python3
"""
analyze_performance.py - Analyze portfolio vs recommendations

Compares actual portfolio performance to recommendations:
- Track recommendation accuracy
- Calculate returns vs market
- Identify best/worst recommendations
- Generate performance reports

Usage:
    python3 analyze_performance.py --report         # Full performance report
    python3 analyze_performance.py --comparison     # Recommendations vs actuals
    python3 analyze_performance.py --assets         # Per-asset analysis
    python3 analyze_performance.py --trends         # Performance trends
"""

import sqlite3
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict

DB_PATH = Path(__file__).parent.parent / 'portfolio_tracker.db'


def get_portfolio_history() -> List[Dict]:
    """Get portfolio value history"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT timestamp, total_value_usd
            FROM portfolio_snapshots
            ORDER BY timestamp
        ''')
        
        history = [
            {
                'timestamp': row[0],
                'value': row[1]
            }
            for row in cursor.fetchall()
        ]
        
        conn.close()
        return history
        
    except Exception as e:
        print(f"✗ Error fetching history: {e}")
        return []


def calculate_returns(days: int = 90) -> Dict:
    """Calculate portfolio returns"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()
        
        cursor.execute('''
            SELECT total_value_usd
            FROM portfolio_snapshots
            WHERE timestamp > ?
            ORDER BY timestamp
            LIMIT 1
        ''', (cutoff,))
        
        oldest = cursor.fetchone()
        
        cursor.execute('''
            SELECT total_value_usd
            FROM portfolio_snapshots
            ORDER BY timestamp DESC
            LIMIT 1
        ''')
        
        newest = cursor.fetchone()
        
        if oldest and newest:
            start_value = oldest[0]
            end_value = newest[0]
            total_return = end_value - start_value
            pct_return = (total_return / start_value * 100) if start_value != 0 else 0
            
            return {
                'period_days': days,
                'start_value': start_value,
                'end_value': end_value,
                'total_return': total_return,
                'pct_return': pct_return
            }
        
        conn.close()
        return {}
        
    except Exception as e:
        print(f"✗ Error calculating returns: {e}")
        return {}


def per_asset_performance() -> Dict:
    """Calculate per-asset performance"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Get latest holdings by asset
        cursor.execute('''
            SELECT DISTINCT asset FROM asset_holdings
        ''')
        
        assets = [row[0] for row in cursor.fetchall()]
        
        performance = {}
        for asset in assets:
            cursor.execute('''
                SELECT ah.value_usd, ps.timestamp
                FROM asset_holdings ah
                JOIN portfolio_snapshots ps ON ah.snapshot_id = ps.id
                WHERE ah.asset = ?
                ORDER BY ps.timestamp
            ''', (asset,))
            
            history = cursor.fetchall()
            
            if history:
                start_value = history[0][0]
                end_value = history[-1][0]
                total_return = end_value - start_value
                pct_return = (total_return / start_value * 100) if start_value != 0 else 0
                
                performance[asset] = {
                    'start_value': start_value,
                    'end_value': end_value,
                    'total_return': total_return,
                    'pct_return': pct_return,
                    'snapshots': len(history)
                }
        
        conn.close()
        return performance
        
    except Exception as e:
        print(f"✗ Error analyzing assets: {e}")
        return {}


def recommendation_accuracy() -> Dict:
    """Analyze recommendation accuracy"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Get all recommendations with outcomes
        cursor.execute('''
            SELECT r.asset, r.action, r.current_price, r.target_price, 
                   r.confidence_score, o.executed, o.execution_price
            FROM recommendations r
            LEFT JOIN recommendation_outcomes o ON r.id = o.recommendation_id
        ''')
        
        rows = cursor.fetchall()
        
        stats = {
            'total': len(rows),
            'executed': 0,
            'met_target': 0,
            'by_asset': {},
            'by_action': {}
        }
        
        for row in rows:
            asset, action, curr, target, conf, executed, exec_price = row
            
            # Initialize asset
            if asset not in stats['by_asset']:
                stats['by_asset'][asset] = {
                    'count': 0,
                    'executed': 0,
                    'met_target': 0,
                    'avg_confidence': 0,
                    'total_confidence': 0
                }
            
            # Initialize action
            if action not in stats['by_action']:
                stats['by_action'][action] = {
                    'count': 0,
                    'executed': 0,
                    'met_target': 0
                }
            
            stats['by_asset'][asset]['count'] += 1
            stats['by_asset'][asset]['total_confidence'] += conf or 0
            stats['by_action'][action]['count'] += 1
            
            if executed:
                stats['executed'] += 1
                stats['by_asset'][asset]['executed'] += 1
                stats['by_action'][action]['executed'] += 1
                
                # Check if target met
                if action == 'SELL' and exec_price >= target:
                    stats['met_target'] += 1
                    stats['by_asset'][asset]['met_target'] += 1
                    stats['by_action'][action]['met_target'] += 1
                elif action == 'BUY' and exec_price <= target:
                    stats['met_target'] += 1
                    stats['by_asset'][asset]['met_target'] += 1
                    stats['by_action'][action]['met_target'] += 1
        
        # Calculate averages
        for asset in stats['by_asset']:
            count = stats['by_asset'][asset]['count']
            if count > 0:
                stats['by_asset'][asset]['avg_confidence'] = \
                    stats['by_asset'][asset]['total_confidence'] / count
        
        stats['accuracy_pct'] = (stats['met_target'] / stats['executed'] * 100) \
            if stats['executed'] > 0 else 0
        
        conn.close()
        return stats
        
    except Exception as e:
        print(f"✗ Error analyzing recommendations: {e}")
        return {}


def print_full_report():
    """Print comprehensive performance report"""
    print("\n" + "=" * 80)
    print("PORTFOLIO PERFORMANCE ANALYSIS".center(80))
    print("=" * 80)
    
    # Overall returns
    print("\n📈 90-Day Returns")
    print("-" * 40)
    returns = calculate_returns(90)
    if returns:
        print(f"Start Value:   ${returns['start_value']:>12.2f}")
        print(f"End Value:     ${returns['end_value']:>12.2f}")
        print(f"Total Return:  ${returns['total_return']:>12.2f}")
        print(f"% Return:      {returns['pct_return']:>12.2f}%")
    
    # Per-asset performance
    print("\n🪙 Per-Asset Performance")
    print("-" * 60)
    print(f"{'Asset':<8} {'Start Value':<15} {'End Value':<15} {'Return %':<12}")
    print("-" * 60)
    
    perf = per_asset_performance()
    for asset, data in sorted(perf.items()):
        print(f"{asset:<8} ${data['start_value']:>12.2f}   ${data['end_value']:>12.2f}   {data['pct_return']:>10.2f}%")
    
    # Recommendation accuracy
    print("\n🎯 Recommendation Accuracy")
    print("-" * 40)
    accuracy = recommendation_accuracy()
    if accuracy['total'] > 0:
        print(f"Total Recommendations: {accuracy['total']}")
        print(f"Executed:              {accuracy['executed']}")
        print(f"Met Target:            {accuracy['met_target']}")
        print(f"Accuracy Rate:         {accuracy['accuracy_pct']:.1f}%")
        
        if accuracy['by_asset']:
            print("\nBy Asset:")
            for asset, stats in accuracy['by_asset'].items():
                acc = (stats['met_target'] / stats['executed'] * 100) \
                    if stats['executed'] > 0 else 0
                print(f"  {asset:<6} {stats['count']:>3} recs, {acc:>5.1f}% accuracy, {stats['avg_confidence']:.2f} conf")
    
    print("\n" + "=" * 80)


def print_asset_trends():
    """Print asset-specific trends"""
    print("\n📊 Asset-Specific Trends")
    print("=" * 80)
    
    perf = per_asset_performance()
    
    # Sort by return percentage
    sorted_assets = sorted(perf.items(), key=lambda x: x[1]['pct_return'], reverse=True)
    
    print("\nTop Performers:")
    for asset, data in sorted_assets[:5]:
        print(f"  🟢 {asset:<6} +{data['pct_return']:.2f}% (${data['total_return']:+.2f})")
    
    print("\nUnderperformers:")
    for asset, data in sorted_assets[-5:]:
        print(f"  🔴 {asset:<6} {data['pct_return']:.2f}% (${data['total_return']:+.2f})")


def main():
    if '--report' in sys.argv:
        print_full_report()
        return 0
    
    elif '--assets' in sys.argv:
        print_asset_trends()
        return 0
    
    elif '--comparison' in sys.argv:
        # Compare recommendations to actuals
        print("\n📋 Recommendation vs Actual Performance")
        print("=" * 80)
        
        accuracy = recommendation_accuracy()
        print(f"\nTotal Recommendations: {accuracy['total']}")
        print(f"Executed: {accuracy['executed']}")
        print(f"Met Target: {accuracy['met_target']}")
        print(f"Accuracy: {accuracy['accuracy_pct']:.1f}%")
        
        return 0
    
    elif '--trends' in sys.argv:
        # Show trends
        history = get_portfolio_history()
        print(f"\n📈 Portfolio Trends ({len(history)} snapshots)")
        print("=" * 60)
        
        if history:
            print(f"First Value: ${history[0]['value']:.2f} ({history[0]['timestamp']})")
            print(f"Last Value:  ${history[-1]['value']:.2f} ({history[-1]['timestamp']})")
            
            total_change = history[-1]['value'] - history[0]['value']
            pct_change = (total_change / history[0]['value'] * 100) if history[0]['value'] != 0 else 0
            
            print(f"Change: ${total_change:+.2f} ({pct_change:+.2f}%)")
        
        return 0
    
    else:
        print("Portfolio Performance Analyzer")
        print("\nUsage:")
        print("  Full report:         python3 analyze_performance.py --report")
        print("  Asset trends:        python3 analyze_performance.py --assets")
        print("  Recommendations:     python3 analyze_performance.py --comparison")
        print("  Price trends:        python3 analyze_performance.py --trends")
        return 1


if __name__ == '__main__':
    sys.exit(main())
