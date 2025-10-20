#!/usr/bin/env python3
"""
fetch_portfolio.py - Kraken Analyst Skill: Portfolio Data Module

Fetches account portfolio data from Kraken private API endpoints.
Requires API key and private key configured in .env file.

Outputs deterministic JSON to stdout for piping to analysis stage.

Usage:
    python fetch_portfolio.py --balances
    python fetch_portfolio.py --open-orders
    python fetch_portfolio.py --trade-history --count 10
    python fetch_portfolio.py --portfolio-summary

Outputs:
    JSON with structure dependent on requested data type

Required Environment Variables:
    KRAKEN_API_KEY - Your Kraken API key
    KRAKEN_PRIVATE_KEY - Your Kraken private key (base64)

API Reference:
    - /private/Balance - Account balances
    - /private/OpenOrders - Open orders
    - /private/TradesHistory - Trade history
    - /private/TradeVolume - Trade volume and fees
"""

import json
import sys
import argparse
import os
from typing import Dict, Optional, List
from kraken_auth import KrakenAuth


class PortfolioFetcher:
    """Fetches portfolio data from Kraken private API"""
    
    def __init__(self):
        self.auth = KrakenAuth()
        
        if not self.auth.is_authenticated():
            print("ERROR: API credentials not configured", file=sys.stderr)
            print("Set KRAKEN_API_KEY and KRAKEN_PRIVATE_KEY in .env file", file=sys.stderr)
            sys.exit(1)
    
    def get_balances(self) -> Optional[Dict]:
        """
        Get account balances
        
        Returns:
            Dictionary of asset balances
        """
        result = self.auth.query_private("Balance")
        
        if result:
            # Convert to cleaner format
            balances = {}
            for asset, amount in result.items():
                balance = float(amount)
                if balance > 0:  # Only include non-zero balances
                    balances[asset] = balance
            
            return {
                "timestamp": self.auth.last_request_time,
                "balances": balances
            }
        
        return None
    
    def get_open_orders(self) -> Optional[Dict]:
        """
        Get open orders
        
        Returns:
            Dictionary of open orders
        """
        result = self.auth.query_private("OpenOrders")
        
        if result:
            return {
                "timestamp": self.auth.last_request_time,
                "open_orders": result.get("open", {})
            }
        
        return None
    
    def get_trade_history(self, count: int = 10, start: Optional[int] = None) -> Optional[Dict]:
        """
        Get trade history
        
        Args:
            count: Number of trades to fetch (max 50)
            start: Start timestamp (optional)
            
        Returns:
            Dictionary of recent trades
        """
        data = {}
        
        if start:
            data["start"] = start
        
        result = self.auth.query_private("TradesHistory", data)
        
        if result:
            trades = result.get("trades", {})
            
            # Sort by time and limit count
            sorted_trades = sorted(
                trades.items(),
                key=lambda x: x[1].get("time", 0),
                reverse=True
            )[:count]
            
            return {
                "timestamp": self.auth.last_request_time,
                "count": len(sorted_trades),
                "trades": dict(sorted_trades)
            }
        
        return None
    
    def get_trade_volume(self) -> Optional[Dict]:
        """
        Get trade volume and fee info
        
        Returns:
            Dictionary with volume and fee information
        """
        result = self.auth.query_private("TradeVolume")
        
        if result:
            return {
                "timestamp": self.auth.last_request_time,
                "currency": result.get("currency", "ZUSD"),
                "volume": result.get("volume", "0"),
                "fees": result.get("fees", {}),
                "fees_maker": result.get("fees_maker", {})
            }
        
        return None
    
    def get_portfolio_summary(self) -> Optional[Dict]:
        """
        Get complete portfolio summary with balances and current prices
        
        Returns:
            Dictionary with portfolio allocation and USD values
        """
        # Get balances
        balances_data = self.get_balances()
        if not balances_data:
            return None
        
        balances = balances_data["balances"]
        portfolio = []
        total_value_usd = 0.0
        
        # Get current prices for each asset
        for asset, amount in balances.items():
            # Skip if stablecoin
            if asset in ["ZUSD", "USD", "USDC", "USDT", "DAI"]:
                portfolio.append({
                    "asset": asset,
                    "amount": amount,
                    "price_usd": 1.0,
                    "value_usd": amount,
                    "weight": 0.0  # Will calculate after total
                })
                total_value_usd += amount
                continue
            
            # Construct trading pair for price lookup
            # Kraken format: XXBTZUSD, XETHZUSD, etc.
            if asset.startswith("X") or asset.startswith("Z"):
                pair = f"{asset}USD"
            else:
                pair = f"{asset}USD"
            
            # Try to get ticker
            ticker_result = self.auth.query_public("Ticker", {"pair": pair})
            
            if ticker_result and pair in ticker_result:
                ticker = ticker_result[pair]
                price_usd = float(ticker["c"][0])  # Last trade price
                value_usd = amount * price_usd
                
                portfolio.append({
                    "asset": asset,
                    "amount": amount,
                    "price_usd": price_usd,
                    "value_usd": value_usd,
                    "weight": 0.0  # Will calculate after total
                })
                
                total_value_usd += value_usd
            else:
                # Can't get price, include with 0 USD value
                portfolio.append({
                    "asset": asset,
                    "amount": amount,
                    "price_usd": None,
                    "value_usd": 0.0,
                    "weight": 0.0
                })
        
        # Calculate weights
        for item in portfolio:
            if total_value_usd > 0:
                item["weight"] = (item["value_usd"] / total_value_usd) * 100
        
        # Sort by value
        portfolio.sort(key=lambda x: x["value_usd"], reverse=True)
        
        return {
            "timestamp": self.auth.last_request_time,
            "total_value_usd": total_value_usd,
            "asset_count": len(portfolio),
            "portfolio": portfolio
        }


def main():
    parser = argparse.ArgumentParser(
        description="Fetch portfolio data from Kraken private API",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--balances",
        action="store_true",
        help="Fetch account balances"
    )
    
    parser.add_argument(
        "--open-orders",
        action="store_true",
        help="Fetch open orders"
    )
    
    parser.add_argument(
        "--trade-history",
        action="store_true",
        help="Fetch trade history"
    )
    
    parser.add_argument(
        "--portfolio-summary",
        action="store_true",
        help="Fetch complete portfolio summary with USD values"
    )
    
    parser.add_argument(
        "--trade-volume",
        action="store_true",
        help="Fetch trade volume and fee info"
    )
    
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of items to fetch (for trade history)"
    )
    
    parser.add_argument(
        "--format",
        choices=["json", "pretty"],
        default="json",
        help="Output format (json or pretty)"
    )
    
    args = parser.parse_args()
    
    # Check if any action specified
    if not any([args.balances, args.open_orders, args.trade_history, 
                args.portfolio_summary, args.trade_volume]):
        parser.print_help()
        sys.exit(1)
    
    # Initialize fetcher
    fetcher = PortfolioFetcher()
    result = None
    
    # Execute requested action
    if args.balances:
        result = fetcher.get_balances()
    elif args.open_orders:
        result = fetcher.get_open_orders()
    elif args.trade_history:
        result = fetcher.get_trade_history(count=args.count)
    elif args.portfolio_summary:
        result = fetcher.get_portfolio_summary()
    elif args.trade_volume:
        result = fetcher.get_trade_volume()
    
    # Output result
    if result:
        if args.format == "pretty":
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result))
    else:
        print("ERROR: Failed to fetch data", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
