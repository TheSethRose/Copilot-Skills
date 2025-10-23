#!/usr/bin/env python3
"""
db_init.py - Initialize SQLite database for portfolio tracking

Creates database schema for:
1. Portfolio snapshots (historical balances)
2. Recommendations log (with confidence scores)
3. Performance tracking (actual vs recommended)
4. Price history (for reference)

Usage:
    python3 db_init.py
    python3 db_init.py --reset  # Recreate tables (WARNING: deletes data)
"""

import sqlite3
import sys
from pathlib import Path
from datetime import datetime

# Database location: same directory as scripts
DB_PATH = Path(__file__).parent.parent / 'portfolio_tracker.db'


def create_tables(conn):
    """Create database schema"""
    cursor = conn.cursor()
    
    # Portfolio snapshots - track holdings over time
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio_snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        total_value_usd REAL NOT NULL,
        spot_value_usd REAL,
        earn_value_usd REAL,
        holdings_json TEXT NOT NULL,
        notes TEXT
    )
    ''')
    
    # Asset holdings - detailed breakdown
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asset_holdings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        snapshot_id INTEGER NOT NULL,
        asset TEXT NOT NULL,
        amount REAL NOT NULL,
        price_usd REAL NOT NULL,
        value_usd REAL NOT NULL,
        allocation_pct REAL NOT NULL,
        source TEXT,
        FOREIGN KEY (snapshot_id) REFERENCES portfolio_snapshots(id)
    )
    ''')
    
    # Recommendations log - track all recommendations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        asset TEXT NOT NULL,
        action TEXT NOT NULL,
        reason TEXT,
        current_price REAL,
        target_price REAL,
        target_allocation_pct REAL,
        confidence_score REAL,
        time_horizon TEXT,
        notes TEXT
    )
    ''')
    
    # Recommendation outcomes - track how recommendations performed
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recommendation_outcomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recommendation_id INTEGER NOT NULL,
        execution_timestamp DATETIME,
        execution_price REAL,
        executed BOOLEAN DEFAULT 0,
        actual_price_change_pct REAL,
        notes TEXT,
        FOREIGN KEY (recommendation_id) REFERENCES recommendations(id)
    )
    ''')
    
    # Technical indicators history - track signals over time
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS technical_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        asset TEXT NOT NULL,
        interval TEXT,
        signal TEXT,
        confidence REAL,
        rsi REAL,
        momentum_sigma REAL,
        volatility_pct REAL,
        ma_trend TEXT,
        support_level REAL,
        resistance_level REAL,
        json_data TEXT
    )
    ''')
    
    # Price snapshots - for historical reference
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        asset TEXT NOT NULL,
        price_usd REAL NOT NULL,
        interval TEXT DEFAULT '1440'
    )
    ''')
    
    # Performance metrics - calculated quarterly/monthly
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS performance_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        period_start DATETIME NOT NULL,
        period_end DATETIME NOT NULL,
        total_return_pct REAL,
        btc_return_pct REAL,
        sol_return_pct REAL,
        dot_return_pct REAL,
        eth_return_pct REAL,
        recommendation_accuracy REAL,
        notes TEXT
    )
    ''')
    
    # Analysis sessions - log each analysis run
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analysis_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        portfolio_value_usd REAL,
        market_condition TEXT,
        overall_signal TEXT,
        analysis_json TEXT,
        notes TEXT
    )
    ''')
    
    conn.commit()
    print("✓ Database schema created successfully")
    return cursor


def create_indexes(conn):
    """Create indexes for faster queries"""
    cursor = conn.cursor()
    
    indexes = [
        'CREATE INDEX IF NOT EXISTS idx_portfolio_timestamp ON portfolio_snapshots(timestamp)',
        'CREATE INDEX IF NOT EXISTS idx_recommendations_asset ON recommendations(asset)',
        'CREATE INDEX IF NOT EXISTS idx_recommendations_timestamp ON recommendations(timestamp)',
        'CREATE INDEX IF NOT EXISTS idx_technical_asset_time ON technical_analysis(asset, timestamp)',
        'CREATE INDEX IF NOT EXISTS idx_price_asset_time ON price_history(asset, timestamp)',
    ]
    
    for index in indexes:
        cursor.execute(index)
    
    conn.commit()
    print("✓ Database indexes created")


def verify_database(db_path):
    """Verify database is working"""
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # Check tables exist
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        )
        tables = cursor.fetchall()
        
        expected_tables = [
            'portfolio_snapshots',
            'asset_holdings',
            'recommendations',
            'recommendation_outcomes',
            'technical_analysis',
            'price_history',
            'performance_metrics',
            'analysis_sessions'
        ]
        
        actual_tables = [t[0] for t in tables]
        
        print(f"\n✓ Database verification:")
        print(f"  Location: {db_path}")
        print(f"  Tables: {len(actual_tables)}/{len(expected_tables)}")
        
        for table in expected_tables:
            status = "✓" if table in actual_tables else "✗"
            print(f"    {status} {table}")
        
        conn.close()
        return all(t in actual_tables for t in expected_tables)
        
    except Exception as e:
        print(f"✗ Database verification failed: {e}")
        return False


def main():
    reset = '--reset' in sys.argv
    
    if reset and DB_PATH.exists():
        print(f"⚠️  Removing existing database: {DB_PATH}")
        DB_PATH.unlink()
        print("✓ Old database removed")
    
    print(f"\n🗄️  Initializing Portfolio Tracker Database")
    print(f"Location: {DB_PATH}")
    
    try:
        conn = sqlite3.connect(str(DB_PATH))
        
        print("\n📋 Creating tables...")
        create_tables(conn)
        
        print("\n📑 Creating indexes...")
        create_indexes(conn)
        
        conn.close()
        
        print("\n✅ Database initialization complete!")
        
        # Verify
        if verify_database(DB_PATH):
            print("\n✅ All verification checks passed!")
            return 0
        else:
            print("\n⚠️  Some verification checks failed")
            return 1
            
    except Exception as e:
        print(f"\n✗ Error initializing database: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
