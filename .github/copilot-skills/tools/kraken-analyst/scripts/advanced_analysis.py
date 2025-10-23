#!/usr/bin/env python3
"""
advanced_analysis.py - Kraken Analyst Skill: Advanced Technical Indicators

Provides sophisticated technical analysis indicators extracted from MaverickMCP patterns.
All indicators work with existing Kraken OHLC data without requiring additional API keys.

Usage:
    python advanced_analysis.py < market_data.json
    python fetch_data.py --pair BTC/USD | python advanced_analysis.py

Features:
    - Support & Resistance level detection
    - ATR (Average True Range) for volatility
    - Stochastic RSI for momentum
    - EMA & WMA moving averages
    - Ichimoku Cloud components
    - Divergence detection (price vs indicators)
    - Advanced volume indicators
"""

import json
import sys
import argparse
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import math


@dataclass
class AdvancedAnalysisResult:
    """Advanced technical analysis output"""
    pair: str
    timestamp: int
    current_price: float
    support_resistance: Dict
    atr: Optional[float]
    stochastic_rsi: Optional[Dict]
    ema: Dict
    ichimoku: Optional[Dict]
    divergences: List[str]
    advanced_signals: List[str]
    
    def to_dict(self):
        return asdict(self)


class AdvancedIndicators:
    """Advanced technical indicator calculations"""
    
    @staticmethod
    def calculate_ema(prices: List[float], period: int) -> List[Optional[float]]:
        """
        Calculate Exponential Moving Average
        More responsive to recent price changes than SMA
        """
        if len(prices) < period:
            return [None] * len(prices)
        
        multiplier = 2 / (period + 1)
        ema: List[Optional[float]] = [None] * (period - 1)  # Pre-fill with None values
        
        # Start with SMA for first calculation
        sma = sum(prices[:period]) / period
        ema.append(sma)
        
        # Calculate EMA for remaining values
        for i in range(period, len(prices)):
            prev_ema = ema[-1]
            if prev_ema is not None:
                ema_value = (prices[i] - prev_ema) * multiplier + prev_ema
                ema.append(ema_value)
            else:
                ema.append(None)
        
        return ema
    
    @staticmethod
    def calculate_wma(prices: List[float], period: int) -> List[Optional[float]]:
        """
        Calculate Weighted Moving Average
        Gives more weight to recent prices
        """
        if len(prices) < period:
            return [None] * len(prices)
        
        wma = []
        weights = list(range(1, period + 1))
        weight_sum = sum(weights)
        
        for i in range(len(prices)):
            if i < period - 1:
                wma.append(None)
            else:
                window = prices[i - period + 1:i + 1]
                wma_value = sum(w * p for w, p in zip(weights, window)) / weight_sum
                wma.append(wma_value)
        
        return wma
    
    @staticmethod
    def calculate_atr(high: List[float], low: List[float], close: List[float], 
                     period: int = 14) -> List[Optional[float]]:
        """
        Calculate Average True Range (ATR)
        Measures market volatility
        """
        if len(high) < period + 1:
            return [None] * len(high)
        
        true_ranges = []
        for i in range(1, len(high)):
            tr = max(
                high[i] - low[i],
                abs(high[i] - close[i-1]),
                abs(low[i] - close[i-1])
            )
            true_ranges.append(tr)
        
        # Calculate ATR using EMA of true ranges
        atr: List[Optional[float]] = [None]  # First value is None
        
        # Initial ATR is SMA of first period TRs
        initial_atr = sum(true_ranges[:period]) / period
        atr.append(initial_atr)
        
        # Subsequent ATRs use smoothing
        for i in range(period, len(true_ranges)):
            prev_atr = atr[-1]
            if prev_atr is not None:
                atr_value = (prev_atr * (period - 1) + true_ranges[i]) / period
                atr.append(atr_value)
            else:
                atr.append(None)
        
        return atr
    
    @staticmethod
    def calculate_stochastic_rsi(prices: List[float], rsi_period: int = 14, 
                                 stoch_period: int = 14, k_period: int = 3, 
                                 d_period: int = 3) -> Optional[Dict]:
        """
        Calculate Stochastic RSI
        More sensitive oscillator than standard RSI
        """
        if len(prices) < rsi_period + stoch_period + k_period + d_period:
            return None
        
        # First calculate RSI
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [max(d, 0) for d in deltas]
        losses = [abs(min(d, 0)) for d in deltas]
        
        rsi_values = []
        for i in range(rsi_period - 1, len(gains)):
            avg_gain = sum(gains[i - rsi_period + 1:i + 1]) / rsi_period
            avg_loss = sum(losses[i - rsi_period + 1:i + 1]) / rsi_period
            
            if avg_loss == 0:
                rsi = 100
            else:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
            rsi_values.append(rsi)
        
        if len(rsi_values) < stoch_period:
            return None
        
        # Apply stochastic calculation to RSI
        stoch_rsi = []
        for i in range(stoch_period - 1, len(rsi_values)):
            window = rsi_values[i - stoch_period + 1:i + 1]
            min_rsi = min(window)
            max_rsi = max(window)
            
            if max_rsi - min_rsi == 0:
                stoch_rsi.append(0)
            else:
                stoch_rsi.append((rsi_values[i] - min_rsi) / (max_rsi - min_rsi) * 100)
        
        # Calculate %K (SMA of Stochastic RSI)
        if len(stoch_rsi) < k_period:
            return None
        
        k_values = []
        for i in range(k_period - 1, len(stoch_rsi)):
            k_values.append(sum(stoch_rsi[i - k_period + 1:i + 1]) / k_period)
        
        # Calculate %D (SMA of %K)
        if len(k_values) < d_period:
            return None
        
        d_values = []
        for i in range(d_period - 1, len(k_values)):
            d_values.append(sum(k_values[i - d_period + 1:i + 1]) / d_period)
        
        return {
            "k": k_values[-1] if k_values else None,
            "d": d_values[-1] if d_values else None,
            "signal": "oversold" if k_values[-1] < 20 else "overbought" if k_values[-1] > 80 else "neutral"
        }
    
    @staticmethod
    def detect_support_resistance(high: List[float], low: List[float], 
                                  close: List[float], threshold: float = 0.02,
                                  lookback: int = 50) -> Dict:
        """
        Detect support and resistance levels
        Uses recent price action to identify key levels
        """
        if len(close) < lookback:
            lookback = len(close)
        
        recent_high = high[-lookback:]
        recent_low = low[-lookback:]
        recent_close = close[-lookback:]
        current_price = close[-1]
        
        # Find potential support levels (local lows)
        support_levels = []
        for i in range(2, len(recent_low) - 2):
            if (recent_low[i] < recent_low[i-1] and recent_low[i] < recent_low[i-2] and
                recent_low[i] < recent_low[i+1] and recent_low[i] < recent_low[i+2]):
                support_levels.append(recent_low[i])
        
        # Find potential resistance levels (local highs)
        resistance_levels = []
        for i in range(2, len(recent_high) - 2):
            if (recent_high[i] > recent_high[i-1] and recent_high[i] > recent_high[i-2] and
                recent_high[i] > recent_high[i+1] and recent_high[i] > recent_high[i+2]):
                resistance_levels.append(recent_high[i])
        
        # Cluster nearby levels
        def cluster_levels(levels, threshold_pct):
            if not levels:
                return []
            levels_sorted = sorted(levels)
            clusters = []
            current_cluster = [levels_sorted[0]]
            
            for level in levels_sorted[1:]:
                if abs(level - current_cluster[-1]) / current_cluster[-1] <= threshold_pct:
                    current_cluster.append(level)
                else:
                    clusters.append(sum(current_cluster) / len(current_cluster))
                    current_cluster = [level]
            clusters.append(sum(current_cluster) / len(current_cluster))
            return clusters
        
        support = cluster_levels(support_levels, threshold)
        resistance = cluster_levels(resistance_levels, threshold)
        
        # Find nearest levels
        nearest_support = max([s for s in support if s < current_price], default=None)
        nearest_resistance = min([r for r in resistance if r > current_price], default=None)
        
        return {
            "support_levels": sorted(support)[-3:] if support else [],  # Top 3 support
            "resistance_levels": sorted(resistance)[:3] if resistance else [],  # Top 3 resistance
            "nearest_support": nearest_support,
            "nearest_resistance": nearest_resistance,
            "distance_to_support": ((current_price - nearest_support) / current_price * 100) if nearest_support else None,
            "distance_to_resistance": ((nearest_resistance - current_price) / current_price * 100) if nearest_resistance else None
        }
    
    @staticmethod
    def calculate_ichimoku(high: List[float], low: List[float], close: List[float]) -> Optional[Dict]:
        """
        Calculate Ichimoku Cloud components
        All-in-one indicator showing support, resistance, trend, and momentum
        """
        if len(high) < 52:  # Need at least 52 periods for Senkou Span B
            return None
        
        def midpoint(data, period):
            """Calculate midpoint of highest high and lowest low"""
            if len(data) < period:
                return None
            window = data[-period:]
            return (max(window) + min(window)) / 2
        
        # Tenkan-sen (Conversion Line): 9-period
        tenkan = midpoint(high[-9:] + low[-9:], 9)
        
        # Kijun-sen (Base Line): 26-period
        kijun = midpoint(high[-26:] + low[-26:], 26)
        
        # Senkou Span A (Leading Span A): (Tenkan + Kijun) / 2, shifted 26 periods ahead
        senkou_a = (tenkan + kijun) / 2 if tenkan and kijun else None
        
        # Senkou Span B (Leading Span B): 52-period midpoint, shifted 26 periods ahead
        senkou_b = midpoint(high[-52:] + low[-52:], 52)
        
        # Chikou Span (Lagging Span): Current close, shifted 26 periods back
        chikou = close[-1]
        
        # Determine cloud color and position
        current_price = close[-1]
        cloud_color = "bullish" if senkou_a and senkou_b and senkou_a > senkou_b else "bearish"
        price_vs_cloud = "above" if current_price > max(senkou_a or 0, senkou_b or 0) else "below" if current_price < min(senkou_a or float('inf'), senkou_b or float('inf')) else "inside"
        
        # Generate signal
        signal = None
        if tenkan and kijun:
            if tenkan > kijun and price_vs_cloud == "above":
                signal = "strong_bullish"
            elif tenkan > kijun:
                signal = "bullish"
            elif tenkan < kijun and price_vs_cloud == "below":
                signal = "strong_bearish"
            elif tenkan < kijun:
                signal = "bearish"
        
        return {
            "tenkan_sen": round(tenkan, 2) if tenkan else None,
            "kijun_sen": round(kijun, 2) if kijun else None,
            "senkou_span_a": round(senkou_a, 2) if senkou_a else None,
            "senkou_span_b": round(senkou_b, 2) if senkou_b else None,
            "chikou_span": round(chikou, 2),
            "cloud_color": cloud_color,
            "price_vs_cloud": price_vs_cloud,
            "signal": signal
        }
    
    @staticmethod
    def detect_divergences(prices: List[float], rsi: List[Optional[float]], 
                          macd: List[Optional[float]], lookback: int = 20) -> List[str]:
        """
        Detect bullish and bearish divergences between price and indicators
        """
        divergences = []
        
        if len(prices) < lookback or len(rsi) < lookback or len(macd) < lookback:
            return divergences
        
        recent_prices = prices[-lookback:]
        recent_rsi = [r for r in rsi[-lookback:] if r is not None]
        recent_macd = [m for m in macd[-lookback:] if m is not None]
        
        if len(recent_rsi) < lookback // 2 or len(recent_macd) < lookback // 2:
            return divergences
        
        # Bullish divergence: price makes lower low, but indicator makes higher low
        price_trend = recent_prices[-1] - recent_prices[0]
        
        if len(recent_rsi) >= 2:
            rsi_trend = recent_rsi[-1] - recent_rsi[0]
            if price_trend < 0 and rsi_trend > 0:
                divergences.append("bullish_rsi_divergence")
        
        if len(recent_macd) >= 2:
            macd_trend = recent_macd[-1] - recent_macd[0]
            if price_trend < 0 and macd_trend > 0:
                divergences.append("bullish_macd_divergence")
        
        # Bearish divergence: price makes higher high, but indicator makes lower high
        if price_trend > 0:
            if len(recent_rsi) >= 2 and recent_rsi[-1] < recent_rsi[0]:
                divergences.append("bearish_rsi_divergence")
            
            if len(recent_macd) >= 2 and recent_macd[-1] < recent_macd[0]:
                divergences.append("bearish_macd_divergence")
        
        return divergences


def analyze_advanced(data: Dict) -> AdvancedAnalysisResult:
    """
    Perform advanced technical analysis on OHLC data
    """
    pair = data.get("pair", "UNKNOWN")
    ohlc_data = data.get("data", [])
    
    if not ohlc_data:
        raise ValueError("No OHLC data provided")
    
    # Extract OHLC arrays - handle both formats
    # Format 1: Array of arrays [timestamp, open, high, low, close, vwap, volume, count]
    # Format 2: Array of objects {timestamp, open, high, low, close, volume, ...}
    
    timestamps = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []
    
    for candle in ohlc_data:
        if isinstance(candle, dict):
            # Object format from fetch_data
            timestamps.append(candle.get("timestamp", 0))
            opens.append(float(candle.get("open", 0)))
            highs.append(float(candle.get("high", 0)))
            lows.append(float(candle.get("low", 0)))
            closes.append(float(candle.get("close", 0)))
            volumes.append(float(candle.get("volume", 0)))
        else:
            # Array format [timestamp, open, high, low, close, vwap, volume, count]
            timestamps.append(candle[0])
            opens.append(float(candle[1]))
            highs.append(float(candle[2]))
            lows.append(float(candle[3]))
            closes.append(float(candle[4]))
            volumes.append(float(candle[6]))
    
    current_price = closes[-1]
    current_timestamp = timestamps[-1]
    
    # Calculate advanced indicators
    indicators = AdvancedIndicators()
    
    # Support & Resistance
    sr = indicators.detect_support_resistance(highs, lows, closes)
    
    # ATR for volatility
    atr_values = indicators.calculate_atr(highs, lows, closes)
    current_atr = atr_values[-1] if atr_values and atr_values[-1] is not None else None
    
    # Stochastic RSI
    stoch_rsi = indicators.calculate_stochastic_rsi(closes)
    
    # Moving averages
    ema_12 = indicators.calculate_ema(closes, 12)
    ema_26 = indicators.calculate_ema(closes, 26)
    wma_20 = indicators.calculate_wma(closes, 20)
    
    ema_dict = {
        "ema_12": ema_12[-1] if ema_12 and ema_12[-1] is not None else None,
        "ema_26": ema_26[-1] if ema_26 and ema_26[-1] is not None else None,
        "wma_20": wma_20[-1] if wma_20 and wma_20[-1] is not None else None,
        "ema_crossover": "bullish" if ema_12 and ema_26 and ema_12[-1] and ema_26[-1] and ema_12[-1] > ema_26[-1] else "bearish"
    }
    
    # Ichimoku Cloud
    ichimoku = indicators.calculate_ichimoku(highs, lows, closes)
    
    # Calculate RSI for divergence detection
    deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    gains = [max(d, 0) for d in deltas]
    losses = [abs(min(d, 0)) for d in deltas]
    
    rsi = []
    rsi_period = 14
    for i in range(rsi_period - 1, len(gains)):
        avg_gain = sum(gains[i - rsi_period + 1:i + 1]) / rsi_period
        avg_loss = sum(losses[i - rsi_period + 1:i + 1]) / rsi_period
        
        if avg_loss == 0:
            rsi.append(100.0)
        else:
            rs = avg_gain / avg_loss
            rsi.append(100 - (100 / (1 + rs)))
    
    # Simple MACD for divergence
    macd_values: List[Optional[float]] = []
    if len(ema_12) > 0 and len(ema_26) > 0:
        for i in range(len(ema_12)):
            val_12 = ema_12[i]
            val_26 = ema_26[i]
            if val_12 is not None and val_26 is not None:
                macd_values.append(val_12 - val_26)
            else:
                macd_values.append(None)
    
    divergences = indicators.detect_divergences(closes, rsi, macd_values)
    
    # Generate advanced signals
    signals = []
    
    # Support/Resistance signals
    if sr.get("distance_to_support") and sr["distance_to_support"] < 2:
        signals.append("near_support_bounce_opportunity")
    if sr.get("distance_to_resistance") and sr["distance_to_resistance"] < 2:
        signals.append("near_resistance_rejection_risk")
    
    # ATR-based volatility signal
    if current_atr:
        atr_percent = (current_atr / current_price) * 100
        if atr_percent > 5:
            signals.append("high_volatility_caution")
        elif atr_percent < 2:
            signals.append("low_volatility_consolidation")
    
    # Stochastic RSI signals
    if stoch_rsi:
        if stoch_rsi.get("signal") == "oversold":
            signals.append("stoch_rsi_oversold_reversal")
        elif stoch_rsi.get("signal") == "overbought":
            signals.append("stoch_rsi_overbought_reversal")
    
    # Ichimoku signals
    if ichimoku and ichimoku.get("signal"):
        signals.append(f"ichimoku_{ichimoku['signal']}")
    
    # Divergence signals
    signals.extend(divergences)
    
    return AdvancedAnalysisResult(
        pair=pair,
        timestamp=current_timestamp,
        current_price=current_price,
        support_resistance=sr,
        atr=current_atr,
        stochastic_rsi=stoch_rsi,
        ema=ema_dict,
        ichimoku=ichimoku,
        divergences=divergences,
        advanced_signals=signals
    )


def main():
    """Main entry point for advanced analysis"""
    parser = argparse.ArgumentParser(description="Advanced technical analysis for crypto")
    parser.add_argument("--format", choices=["json", "text"], default="json",
                       help="Output format")
    args = parser.parse_args()
    
    try:
        # Read market data from stdin
        input_data = json.load(sys.stdin)
        
        # Perform advanced analysis
        result = analyze_advanced(input_data)
        
        if args.format == "json":
            print(json.dumps(result.to_dict(), indent=2))
        else:
            # Text format
            print(f"\n{'='*60}")
            print(f"ADVANCED TECHNICAL ANALYSIS: {result.pair}")
            print(f"{'='*60}\n")
            
            print(f"Current Price: ${result.current_price:,.2f}")
            print(f"Timestamp: {result.timestamp}\n")
            
            # Support & Resistance
            sr = result.support_resistance
            print("📊 Support & Resistance:")
            if sr.get("nearest_support"):
                print(f"  Nearest Support: ${sr['nearest_support']:,.2f} ({sr.get('distance_to_support', 0):.2f}% away)")
            if sr.get("nearest_resistance"):
                print(f"  Nearest Resistance: ${sr['nearest_resistance']:,.2f} ({sr.get('distance_to_resistance', 0):.2f}% away)")
            print()
            
            # ATR
            if result.atr:
                atr_pct = (result.atr / result.current_price) * 100
                print(f"📈 ATR (Volatility): ${result.atr:.2f} ({atr_pct:.2f}%)")
                print()
            
            # Stochastic RSI
            if result.stochastic_rsi:
                print("🎯 Stochastic RSI:")
                print(f"  %K: {result.stochastic_rsi['k']:.2f}")
                print(f"  %D: {result.stochastic_rsi['d']:.2f}")
                print(f"  Signal: {result.stochastic_rsi['signal'].upper()}")
                print()
            
            # Ichimoku
            if result.ichimoku:
                ich = result.ichimoku
                print("☁️  Ichimoku Cloud:")
                print(f"  Tenkan-sen: ${ich['tenkan_sen']}")
                print(f"  Kijun-sen: ${ich['kijun_sen']}")
                print(f"  Cloud: {ich['cloud_color'].upper()}")
                print(f"  Price vs Cloud: {ich['price_vs_cloud'].upper()}")
                if ich.get('signal'):
                    print(f"  Signal: {ich['signal'].upper()}")
                print()
            
            # Signals
            if result.advanced_signals:
                print("🚨 Advanced Signals:")
                for signal in result.advanced_signals:
                    print(f"  • {signal.replace('_', ' ').title()}")
                print()
            
            # Divergences
            if result.divergences:
                print("⚠️  Divergences Detected:")
                for div in result.divergences:
                    print(f"  • {div.replace('_', ' ').title()}")
                print()
    
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        import traceback
        print(f"Error: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
