#!/usr/bin/env python3
"""
log_recommendations.py - Log portfolio recommendations to database

Saves recommendations with:
- Specific asset and action (BUY/SELL)
- Target price and allocation
- Confidence score and reasoning
- Time horizon and notes

This allows tracking recommendation accuracy over time.

Usage:
    python3 log_recommendations.py --log BTC SELL 112000 0.2 0.85 "Rally target"
    python3 log_recommendations.py --review         # Show recent recommendations
    python3 log_recommendations.py --accuracy       # Calculate accuracy metrics
"""

import sqlite3
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

DB_PATH = Path(__file__).parent.parent / 'portfolio_tracker.db'


def log_recommendation(
    asset: str,
    action: str,
    current_price: float,
    target_price: float,
    target_allocation_pct: Optional[float] = None,
    confidence: float = 0.5,
    time_horizon: str = "4-weeks",
    reason: str = "",
    notes: str = ""
) -> int:
    """
    Log a recommendation to the database
    
    Args:
        asset: Cryptocurrency symbol (BTC, ETH, SOL, DOT)
        action: BUY, SELL, HOLD, or REDUCE
        current_price: Current price in USD
        target_price: Target price for this recommendation
        target_allocation_pct: Target % of portfolio
        confidence: Confidence score 0.0-1.0
        time_horizon: "days", "weeks", "months"
        reason: Why this recommendation
        notes: Additional context
    
    Returns:
        Recommendation ID if successful, None otherwise
    """
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO recommendations
            (asset, action, reason, current_price, target_price, 
             target_allocation_pct, confidence_score, time_horizon, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            asset.upper(),
            action.upper(),
            reason,
            current_price,
            target_price,
            target_allocation_pct,
            confidence,
            time_horizon,
            notes
        ))
        
        rec_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return rec_id
        
    except Exception as e:
        print(f"✗ Error logging recommendation: {e}")
        return None


def review_recommendations(days: int = 30, asset: Optional[str] = None):
    """Review recent recommendations"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        query = '''
            SELECT id, timestamp, asset, action, current_price, target_price,
                   confidence_score, time_horizon, reason
            FROM recommendations
            WHERE datetime(timestamp) > datetime('now', '-' || ? || ' days')
        '''
        params = [days]
        
        if asset:
            query += ' AND asset = ?'
            params.append(asset.upper())
        
        query += ' ORDER BY timestamp DESC'
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        print(f"\n📋 Recommendations (Last {days} days)")
        print("=" * 110)
        print(f"{'ID':<4} {'Date':<19} {'Asset':<6} {'Action':<7} {'Current':<12} {'Target':<12} {'Conf':<6} {'Horizon':<12}")
        print("-" * 110)
        
        for row in rows:
            rec_id, timestamp, asset_sym, action, curr, target, conf, horizon, reason = row
            dt = datetime.fromisoformat(timestamp)
            display_time = dt.strftime('%Y-%m-%d %H:%M')
            
            # Calculate expected move
            if curr and target:
                move_pct = ((target - curr) / curr * 100)
                move_str = f"{move_pct:+.1f}%"
            else:
                move_str = "N/A"
            
            print(f"{rec_id:<4} {display_time:<19} {asset_sym:<6} {action:<7} ${curr:>10.2f} ${target:>10.2f} {conf:>5.2f} {horizon:<12}")
            if reason:
                print(f"      └─ {reason}")
        
        conn.close()
        
        if not rows:
            print(f"No recommendations found for the last {days} days")
        
    except Exception as e:
        print(f"✗ Error reviewing recommendations: {e}")


def calculate_accuracy(days: int = 90):
    """Calculate recommendation accuracy"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        # Get recommendations with outcomes
        cursor.execute('''
            SELECT r.id, r.asset, r.action, r.current_price, r.target_price, 
                   r.confidence_score, o.executed, o.execution_price
            FROM recommendations r
            LEFT JOIN recommendation_outcomes o ON r.id = o.recommendation_id
            WHERE datetime(r.timestamp) > datetime('now', '-' || ? || ' days')
        ''', [days])
        
        rows = cursor.fetchall()
        
        print(f"\n📊 Recommendation Accuracy (Last {days} days)")
        print("=" * 80)
        
        if not rows:
            print("No recommendations to analyze")
            conn.close()
            return
        
        total = len(rows)
        executed = sum(1 for r in rows if r[6])
        correct = 0
        
        for row in rows:
            rec_id, asset, action, curr, target, conf, executed_flag, exec_price = row
            
            if executed_flag and exec_price:
                # Check if target was hit
                if action == 'SELL':
                    if exec_price >= target:
                        correct += 1
                elif action == 'BUY':
                    if exec_price <= target:
                        correct += 1
        
        accuracy_pct = (correct / executed * 100) if executed > 0 else 0
        
        print(f"Total Recommendations: {total}")
        print(f"Executed: {executed}")
        print(f"Met Target: {correct}")
        print(f"Accuracy: {accuracy_pct:.1f}%")
        
        # By asset
        cursor.execute('''
            SELECT asset, COUNT(*) as count, AVG(confidence_score) as avg_conf
            FROM recommendations
            WHERE datetime(timestamp) > datetime('now', '-' || ? || ' days')
            GROUP BY asset
        ''', [days])
        
        print("\nBy Asset:")
        print("-" * 40)
        for asset, count, avg_conf in cursor.fetchall():
            print(f"  {asset:<6} {count:>3} recommendations, avg confidence {avg_conf:.2f}")
        
        conn.close()
        
    except Exception as e:
        print(f"✗ Error calculating accuracy: {e}")


def mark_executed(rec_id: int, execution_price: float, notes: str = ""):
    """Mark a recommendation as executed"""
    try:
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO recommendation_outcomes
            (recommendation_id, execution_timestamp, execution_price, executed, notes)
            VALUES (?, datetime('now'), ?, 1, ?)
        ''', (rec_id, execution_price, notes))
        
        conn.commit()
        conn.close()
        
        print(f"✓ Marked recommendation {rec_id} as executed at ${execution_price:.2f}")
        return True
        
    except Exception as e:
        print(f"✗ Error marking as executed: {e}")
        return False


def main():
    if '--log' in sys.argv:
        # Log new recommendation
        idx = sys.argv.index('--log')
        if idx + 4 < len(sys.argv):
            asset = sys.argv[idx + 1]
            action = sys.argv[idx + 2]
            current = float(sys.argv[idx + 3])
            target = float(sys.argv[idx + 4])
            confidence = float(sys.argv[idx + 5]) if idx + 5 < len(sys.argv) else 0.5
            reason = sys.argv[idx + 6] if idx + 6 < len(sys.argv) else ""
            
            rec_id = log_recommendation(
                asset=asset,
                action=action,
                current_price=current,
                target_price=target,
                confidence=confidence,
                reason=reason
            )
            
            if rec_id:
                print(f"✓ Recommendation logged (ID: {rec_id})")
                return 0
        else:
            print("Usage: python3 log_recommendations.py --log ASSET ACTION CURRENT TARGET [CONFIDENCE] [REASON]")
            return 1
    
    elif '--review' in sys.argv:
        # Review recommendations
        days = 30
        asset = None
        if '--days' in sys.argv:
            idx = sys.argv.index('--days')
            days = int(sys.argv[idx + 1])
        if '--asset' in sys.argv:
            idx = sys.argv.index('--asset')
            asset = sys.argv[idx + 1]
        
        review_recommendations(days, asset)
        return 0
    
    elif '--accuracy' in sys.argv:
        # Calculate accuracy
        days = 90
        if '--days' in sys.argv:
            idx = sys.argv.index('--days')
            days = int(sys.argv[idx + 1])
        
        calculate_accuracy(days)
        return 0
    
    elif '--executed' in sys.argv:
        # Mark as executed
        idx = sys.argv.index('--executed')
        if idx + 2 < len(sys.argv):
            rec_id = int(sys.argv[idx + 1])
            exec_price = float(sys.argv[idx + 2])
            mark_executed(rec_id, exec_price)
            return 0
    
    else:
        print("Portfolio Recommendation Logger")
        print("\nUsage:")
        print("  Log recommendation:")
        print("    python3 log_recommendations.py --log BTC SELL 112000 0.2 0.85 'Rally target'")
        print("\n  Review recommendations:")
        print("    python3 log_recommendations.py --review [--days 30] [--asset BTC]")
        print("\n  Calculate accuracy:")
        print("    python3 log_recommendations.py --accuracy [--days 90]")
        print("\n  Mark as executed:")
        print("    python3 log_recommendations.py --executed <id> <execution_price>")
        return 1


if __name__ == '__main__':
    sys.exit(main())
