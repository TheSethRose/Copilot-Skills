#!/usr/bin/env python3
"""
fetch_data.py - Kraken Analyst Skill: Data Fetching Module

Fetches OHLC candle data from Kraken REST API v0.
Based on official Kraken API documentation: https://docs.kraken.com/api/

Outputs deterministic JSON to stdout for piping to next analysis stage.

Usage:
    python fetch_data.py --pair XBTUSD --interval 60 --count 100
    python fetch_data.py --pair ETHUSD --interval 3600 --count 50
    python fetch_data.py --list-pairs

Outputs:
    JSON with structure: { pair, interval, data: [{ timestamp, open, high, low, close, volume }] }

API Reference:
    - Endpoint: GET https://api.kraken.com/0/public/OHLC
    - Parameters: pair (required), interval (optional, default 1), since (optional)
    - Returns: Up to 720 most recent OHLC entries
"""

import json
import sys
import argparse
import time
from typing import List, Dict, Optional
import urllib.parse
import urllib.request
from datetime import datetime


class KrakenDataFetcher:
    """Fetches OHLC data from Kraken REST API"""
    
    BASE_URL = "https://api.kraken.com/0/public"
    
    # Valid intervals in minutes (Kraken API spec)
    VALID_INTERVALS = {
        1: "1m",
        5: "5m",
        15: "15m",
        30: "30m",
        60: "1h",
        240: "4h",
        1440: "1d",
        10080: "1w",
        21600: "15d"
    }
    
    # Kraken pair format (no slash, X prefix for crypto, Z prefix for fiat)
    # Source: https://docs.kraken.com/api/docs/rest-api/get-tradable-asset-pairs
    COMMON_PAIRS = {
        # Major BTC pairs
        "BTC/USD": "XXBTZUSD",
        "BTC/EUR": "XXBTZEUR",
        "BTC/GBP": "XXBTZGBP",
        # ETH pairs
        "ETH/USD": "XETHZUSD",
        "ETH/EUR": "XETHZEUR",
        "ETH/BTC": "XETHXXBT",
        # Other major crypto
        "XRP/USD": "XXRPZUSD",
        "XRP/EUR": "XXRPZEUR",
        "LTC/USD": "XLTCZUSD",
        "LTC/EUR": "XLTCZEUR",
        "ADA/USD": "ADAUSD",
        "ADA/EUR": "ADAEUR",
        "SOL/USD": "SOLUSD",
        "SOL/EUR": "SOLEUR",
        "DOT/USD": "DOTUSD",
        "DOT/EUR": "DOTEUR",
        "LINK/USD": "LINKUSD",
        "DOGE/USD": "XDGUSD",
        "MATIC/USD": "MATICUSD",
    }
    
    def __init__(self, rate_limit: float = 0.5):
        """
        Initialize fetcher.
        
        Args:
            rate_limit: Seconds to wait between requests (Kraken recommends 0.5+)
        """
        self.rate_limit = rate_limit
        self.last_request_time = 0
    
    def _rate_limit_wait(self):
        """Enforce rate limiting between API calls"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self.last_request_time = time.time()
    
    def _normalize_pair(self, pair: str) -> str:
        """
        Convert user-friendly pair format to Kraken API format.
        
        Examples:
            BTC/USD -> XXBTZUSD
            ETH/EUR -> XETHZEUR
            ADAUSD -> ADAUSD (already in correct format)
        """
        # Check if already in Kraken format (no slash)
        if '/' not in pair:
            return pair.upper()
        
        # Look up in common pairs
        if pair.upper() in self.COMMON_PAIRS:
            return self.COMMON_PAIRS[pair.upper()]
        
        # Try to construct it
        base, quote = pair.upper().split('/')
        
        # Add X prefix for standard crypto
        if base in ["BTC", "ETH", "LTC", "XRP", "XLM", "XTZ", "DOT", "ATOM"]:
            base = f"X{base}"
        
        # Add Z prefix for fiat
        if quote in ["USD", "EUR", "GBP", "JPY", "CAD", "CHF", "AUD"]:
            quote = f"Z{quote}"
        
        return f"{base}{quote}"
    
    def validate_interval(self, interval: int) -> bool:
        """Validate that interval is supported"""
        return interval in self.VALID_INTERVALS
    
    def fetch_ohlc(self, pair: str, interval: int, count: int) -> Optional[Dict]:
        """
        Fetch OHLC data from Kraken API.
        
        Args:
            pair: Trading pair (e.g., "BTC/USD" or "XXBTZUSD")
            interval: Candle interval in minutes
            count: Number of candles to fetch (max 720)
        
        Returns:
            Dict with { pair, interval, data: [candles] } or None on error
        """
        # Validate interval
        if not self.validate_interval(interval):
            print(f"ERROR: Invalid interval {interval}. Valid: {list(self.VALID_INTERVALS.keys())}", 
                  file=sys.stderr)
            return None
        
        if not (1 <= count <= 720):
            print(f"ERROR: Count must be 1-720, got {count}", file=sys.stderr)
            return None
        
        # Normalize pair format
        api_pair = self._normalize_pair(pair)
        
        try:
            # Rate limit before request
            self._rate_limit_wait()
            
            # Build request URL
            params = {
                "pair": api_pair,
                "interval": interval
            }
            
            url = f"{self.BASE_URL}/OHLC?{urllib.parse.urlencode(params)}"
            
            # Make API request (using urllib to avoid external dependencies)
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Kraken-Analyst-Skill/1.0')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
            
            # Check for API errors
            if data.get('error') and len(data['error']) > 0:
                print(f"ERROR: Kraken API error: {data['error']}", file=sys.stderr)
                return None
            
            # Extract result
            result = data.get('result', {})
            
            # Find the pair key (Kraken returns it with their naming)
            pair_key = None
            for key in result.keys():
                if key != 'last':
                    pair_key = key
                    break
            
            if not pair_key:
                print(f"ERROR: No OHLC data found for pair {pair}", file=sys.stderr)
                return None
            
            candles_raw = result[pair_key]
            
            # Limit to requested count (newest first)
            candles_raw = candles_raw[-count:]
            
            # Format output
            # Kraken OHLC format: [time, open, high, low, close, vwap, volume, count]
            formatted_candles = []
            for candle in candles_raw:
                formatted_candles.append({
                    "timestamp": int(candle[0]),
                    "datetime": datetime.utcfromtimestamp(int(candle[0])).isoformat(),
                    "open": float(candle[1]),
                    "high": float(candle[2]),
                    "low": float(candle[3]),
                    "close": float(candle[4]),
                    "vwap": float(candle[5]),
                    "volume": float(candle[6]),
                    "count": int(candle[7])
                })
            
            return {
                "pair": pair,
                "pair_kraken": api_pair,
                "interval": interval,
                "interval_name": self.VALID_INTERVALS[interval],
                "data_points": len(formatted_candles),
                "timestamp": datetime.utcnow().isoformat(),
                "source": "Kraken REST API v0",
                "data": formatted_candles
            }
        
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"ERROR: Rate limited by Kraken. Increase --rate-limit", file=sys.stderr)
            else:
                print(f"ERROR: HTTP {e.code}: {e.reason}", file=sys.stderr)
            return None
        except urllib.error.URLError as e:
            print(f"ERROR: Failed to connect to Kraken API: {e.reason}", file=sys.stderr)
            return None
        except Exception as e:
            print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
            return None
    
    def list_supported_pairs(self) -> str:
        """Return formatted list of supported pairs"""
        pairs = sorted(self.COMMON_PAIRS.keys())
        return ", ".join(pairs)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch OHLC data from Kraken REST API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fetch_data.py --pair BTC/USD --interval 60 --count 100
  python fetch_data.py --pair XXBTZUSD --interval 1440 --count 30
  python fetch_data.py --list-pairs
  python fetch_data.py --list-intervals
        """
    )
    
    parser.add_argument(
        "--pair",
        type=str,
        help="Trading pair (e.g., BTC/USD, ETH/EUR, or XXBTZUSD)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Candle interval in minutes: 1, 5, 15, 30, 60, 240, 1440, 10080, 21600 (default: 60)"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=100,
        help="Number of candles to fetch (1-720, default: 100)"
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=0.5,
        help="Seconds between API requests (default: 0.5)"
    )
    parser.add_argument(
        "--list-pairs",
        action="store_true",
        help="List all supported trading pairs"
    )
    parser.add_argument(
        "--list-intervals",
        action="store_true",
        help="List all supported intervals"
    )
    
    args = parser.parse_args()
    
    fetcher = KrakenDataFetcher(rate_limit=args.rate_limit)
    
    # Handle list commands
    if args.list_pairs:
        print(fetcher.list_supported_pairs())
        return 0
    
    if args.list_intervals:
        intervals = ", ".join(
            f"{interval} min ({name})" 
            for interval, name in sorted(fetcher.VALID_INTERVALS.items())
        )
        print(intervals)
        return 0
    
    # Require pair for normal operation
    if not args.pair:
        parser.print_help()
        return 1
    
    # Fetch data
    result = fetcher.fetch_ohlc(args.pair, args.interval, args.count)
    
    if result:
        # Output JSON to stdout for piping
        print(json.dumps(result, indent=2))
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
