#!/usr/bin/env python3
"""
apply_rules.py - Kraken Analyst Skill: Analysis Rules Module

Applies quantitative rule-sets to OHLC data for strategy signals.
Reads JSON from stdin (from fetch_data.py), outputs analysis JSON to stdout.

Usage:
    python apply_rules.py < market_data.json
    python fetch_data.py --pair BTC/USD | python apply_rules.py

Outputs:
    JSON with analysis results, signal, and confidence score
"""

import json
import sys
import argparse
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict


@dataclass
class AnalysisResult:
    """Holds analysis output for JSON serialization"""
    pair: str
    timestamp: int
    current_price: float
    analysis: Dict
    signal: str
    confidence: float
    
    def to_dict(self):
        return asdict(self)


class KrakenAnalyzer:
    """Applies trading rules and generates signals"""
    
    def __init__(self, momentum_threshold: float = 2.0, 
                 volatility_threshold: float = 2.5,
                 rsi_period: int = 14,
                 ma_fast: int = 12,
                 ma_slow: int = 26):
        """
        Initialize analyzer with configurable thresholds.
        
        Args:
            momentum_threshold: Standard deviations for momentum signal
            volatility_threshold: Annualized volatility threshold (%)
            rsi_period: Period for RSI calculation
            ma_fast: Fast moving average period
            ma_slow: Slow moving average period
        """
        self.momentum_threshold = momentum_threshold
        self.volatility_threshold = volatility_threshold
        self.rsi_period = rsi_period
        self.ma_fast = ma_fast
        self.ma_slow = ma_slow
    
    def calculate_moving_average(self, prices: List[float], period: int) -> List[Optional[float]]:
        """Calculate simple moving average"""
        if len(prices) < period:
            return [None] * len(prices)
        
        ma = []
        for i in range(len(prices)):
            if i < period - 1:
                ma.append(None)
            else:
                window = prices[i - period + 1:i + 1]
                ma.append(sum(window) / period)
        return ma
    
    def calculate_rsi(self, prices: List[float], period: int = 14) -> List[Optional[float]]:
        """Calculate Relative Strength Index"""
        if len(prices) < period + 1:
            return [None] * len(prices)
        
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [max(d, 0) for d in deltas]
        losses = [-min(d, 0) for d in deltas]
        
        rsi = [None]  # First value has no delta
        for i in range(len(prices) - 1):
            if i < period - 1:
                rsi.append(None)
            else:
                avg_gain = sum(gains[i-period+1:i+1]) / period
                avg_loss = sum(losses[i-period+1:i+1]) / period
                
                if avg_loss == 0:
                    rs = 100 if avg_gain > 0 else 50
                else:
                    rs = avg_gain / avg_loss
                
                rsi_value = 100 - (100 / (1 + rs))
                rsi.append(rsi_value)
        
        return rsi
    
    def calculate_volatility(self, prices: List[float], period: int = 20) -> float:
        """Calculate annualized volatility"""
        if len(prices) < period:
            return 0.0
        
        recent_prices = prices[-period:]
        returns = []
        
        for i in range(1, len(recent_prices)):
            ret = (recent_prices[i] - recent_prices[i-1]) / recent_prices[i-1]
            returns.append(ret)
        
        if not returns:
            return 0.0
        
        mean_return = sum(returns) / len(returns)
        variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
        std_dev = variance ** 0.5
        
        # Annualize: sqrt(252 trading days per year)
        annualized_vol = std_dev * (252 ** 0.5) * 100
        
        return annualized_vol
    
    def calculate_momentum(self, prices: List[float], ma_period: int = 50) -> float:
        """Calculate momentum as price deviation from MA in std devs"""
        if len(prices) < ma_period + 20:
            return 0.0
        
        recent_prices = prices[-(ma_period + 20):]
        ma = sum(recent_prices[:ma_period]) / ma_period
        current_price = recent_prices[-1]
        
        # Calculate std dev over 20 most recent periods
        deviations = [(p - ma) ** 2 for p in recent_prices[-20:]]
        std_dev = (sum(deviations) / 20) ** 0.5
        
        if std_dev == 0:
            return 0.0
        
        momentum = (current_price - ma) / std_dev
        return round(momentum, 2)
    
    def analyze(self, ohlc_data: Dict) -> Optional[AnalysisResult]:
        """
        Perform complete analysis on OHLC data.
        
        Args:
            ohlc_data: Dict with pair, interval, data: [candles]
        
        Returns:
            AnalysisResult with signal and confidence
        """
        try:
            pair = ohlc_data.get('pair', 'UNKNOWN')
            candles = ohlc_data.get('data', [])
            
            if not candles or len(candles) < self.ma_slow + 20:
                print(f"ERROR: Insufficient data. Need at least {self.ma_slow + 20} candles, got {len(candles)}", 
                      file=sys.stderr)
                return None
            
            # Extract prices
            closes = [c['close'] for c in candles]
            opens = [c['open'] for c in candles]
            highs = [c['high'] for c in candles]
            lows = [c['low'] for c in candles]
            volumes = [c['volume'] for c in candles]
            
            # Calculate indicators
            ma_fast_vals = self.calculate_moving_average(closes, self.ma_fast)
            ma_slow_vals = self.calculate_moving_average(closes, self.ma_slow)
            rsi_vals = self.calculate_rsi(closes, self.rsi_period)
            
            # Current values (last candle)
            current_close = closes[-1]
            current_rsi = rsi_vals[-1] if rsi_vals[-1] is not None else 50
            current_ma_fast = ma_fast_vals[-1] if ma_fast_vals[-1] is not None else current_close
            current_ma_slow = ma_slow_vals[-1] if ma_slow_vals[-1] is not None else current_close
            
            momentum = self.calculate_momentum(closes)
            volatility = self.calculate_volatility(closes)
            
            # Determine trend
            if current_ma_fast > current_ma_slow:
                ma_trend = "bullish"
            elif current_ma_fast < current_ma_slow:
                ma_trend = "bearish"
            else:
                ma_trend = "neutral"
            
            # Calculate price change
            price_change = ((current_close - opens[0]) / opens[0]) * 100
            
            # Generate signal using rule-based logic
            signal, base_confidence = self._generate_signal(
                momentum, current_rsi, ma_trend, volatility
            )
            
            # Adjust confidence based on factors
            confidence = self._calculate_confidence(
                momentum, current_rsi, volatility, volumes[-10:], base_confidence
            )
            
            analysis = {
                "momentum": momentum,
                "momentum_threshold": self.momentum_threshold,
                "volatility": round(volatility, 2),
                "volatility_threshold": self.volatility_threshold,
                "rsi": round(current_rsi, 1),
                "rsi_period": self.rsi_period,
                "ma_fast": round(current_ma_fast, 2),
                "ma_slow": round(current_ma_slow, 2),
                "ma_signal": ma_trend,
                "price_change_pct": round(price_change, 2),
                "recent_volume": round(volumes[-1], 2),
                "avg_volume": round(sum(volumes[-10:]) / 10, 2),
                "volume_ratio": round(volumes[-1] / (sum(volumes[-10:]) / 10), 2) if sum(volumes[-10:]) > 0 else 1.0
            }
            
            result = AnalysisResult(
                pair=pair,
                timestamp=int(candles[-1]['timestamp']),
                current_price=round(current_close, 2),
                analysis=analysis,
                signal=signal,
                confidence=round(confidence, 3)
            )
            
            return result
        
        except Exception as e:
            print(f"ERROR: Analysis failed: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            return None
    
    def _generate_signal(self, momentum: float, rsi: float, 
                         ma_trend: str, volatility: float) -> Tuple[str, float]:
        """
        Primary signal generation rule logic.
        
        Returns: (signal, base_confidence)
        """
        # Strong BUY conditions
        if (momentum > self.momentum_threshold and 
            rsi < 70 and 
            ma_trend == "bullish" and
            volatility < self.volatility_threshold * 1.5):
            return "BUY", 0.8
        
        # Strong SELL conditions
        if (momentum < -self.momentum_threshold and 
            rsi > 30 and 
            ma_trend == "bearish" and
            volatility < self.volatility_threshold * 1.5):
            return "SELL", 0.8
        
        # Moderate BUY
        if momentum > self.momentum_threshold and rsi < 80:
            return "BUY", 0.5
        
        # Moderate SELL
        if momentum < -self.momentum_threshold and rsi > 20:
            return "SELL", 0.5
        
        # Hold/Neutral
        return "HOLD", 0.5
    
    def _calculate_confidence(self, momentum: float, rsi: float, 
                             volatility: float, recent_volumes: List[float],
                             base_confidence: float) -> float:
        """
        Calculate final confidence score with adjustments.
        """
        confidence = base_confidence
        
        # Adjust for volatility
        if volatility > 0:
            vol_factor = max(0.5, 1.0 - (volatility / 10.0))
            confidence *= vol_factor
        
        # Adjust for RSI extremes
        if rsi > 75 or rsi < 25:
            confidence *= 0.8  # Extreme RSI = uncertain
        
        # Adjust for volume confirmation
        if recent_volumes and len(recent_volumes) > 0:
            avg_vol = sum(recent_volumes) / len(recent_volumes)
            current_vol = recent_volumes[-1]
            if avg_vol > 0:
                if current_vol > avg_vol * 1.5:
                    confidence *= 1.1  # High volume = more certain
                elif current_vol < avg_vol * 0.5:
                    confidence *= 0.8  # Low volume = less certain
        
        # Clamp to valid range
        return max(0.0, min(1.0, confidence))


def main():
    parser = argparse.ArgumentParser(
        description="Apply analysis rules to OHLC data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python apply_rules.py < market_data.json
  python fetch_data.py --pair BTC/USD | python apply_rules.py
  python apply_rules.py --momentum-threshold 1.5 --volatility-threshold 3.0 < data.json
        """
    )
    
    parser.add_argument(
        "--momentum-threshold",
        type=float,
        default=2.0,
        help="Standard deviations for momentum signal (default: 2.0)"
    )
    parser.add_argument(
        "--volatility-threshold",
        type=float,
        default=2.5,
        help="Annualized volatility threshold (default: 2.5)"
    )
    parser.add_argument(
        "--rsi-period",
        type=int,
        default=14,
        help="RSI calculation period (default: 14)"
    )
    parser.add_argument(
        "--ma-fast",
        type=int,
        default=12,
        help="Fast moving average period (default: 12)"
    )
    parser.add_argument(
        "--ma-slow",
        type=int,
        default=26,
        help="Slow moving average period (default: 26)"
    )
    
    args = parser.parse_args()
    
    # Read JSON from stdin
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON input: {e}", file=sys.stderr)
        return 1
    
    # Run analysis
    analyzer = KrakenAnalyzer(
        momentum_threshold=args.momentum_threshold,
        volatility_threshold=args.volatility_threshold,
        rsi_period=args.rsi_period,
        ma_fast=args.ma_fast,
        ma_slow=args.ma_slow
    )
    
    result = analyzer.analyze(input_data)
    
    if result:
        print(json.dumps(result.to_dict(), indent=2))
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
