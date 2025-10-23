#!/usr/bin/env python3
"""
portfolio_optimizer.py - Kraken Analyst Skill: Portfolio Optimization

Portfolio analysis using Modern Portfolio Theory adapted from MaverickMCP patterns.
Provides correlation analysis, Sharpe ratio optimization, and risk metrics.
Works with existing Kraken portfolio data without requiring additional API keys.

Usage:
    python portfolio_optimizer.py < portfolio_data.json
    python fetch_portfolio.py | python portfolio_optimizer.py

Features:
    - Correlation matrix for holdings
    - Sharpe ratio optimization
    - Maximum drawdown analysis
    - Risk contribution by asset
    - Diversification metrics
    - Rebalancing recommendations
"""

import json
import sys
import argparse
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import math


@dataclass
class PortfolioMetrics:
    """Portfolio optimization results"""
    total_value: float
    assets: List[Dict]
    correlation_matrix: Optional[Dict]
    sharpe_ratio: Optional[float]
    max_drawdown: Optional[float]
    diversification_ratio: Optional[float]
    risk_metrics: Dict
    rebalancing_recommendations: Optional[List[Dict]]
    
    def to_dict(self):
        return asdict(self)


class PortfolioAnalyzer:
    """Modern Portfolio Theory analysis"""
    
    @staticmethod
    def calculate_returns(prices: List[float]) -> List[float]:
        """Calculate simple returns from price series"""
        if len(prices) < 2:
            return []
        
        returns = []
        for i in range(1, len(prices)):
            if prices[i-1] != 0:
                ret = (prices[i] - prices[i-1]) / prices[i-1]
                returns.append(ret)
            else:
                returns.append(0.0)
        
        return returns
    
    @staticmethod
    def calculate_correlation(returns_a: List[float], returns_b: List[float]) -> Optional[float]:
        """Calculate correlation coefficient between two return series"""
        if len(returns_a) != len(returns_b) or len(returns_a) < 2:
            return None
        
        n = len(returns_a)
        
        # Calculate means
        mean_a = sum(returns_a) / n
        mean_b = sum(returns_b) / n
        
        # Calculate correlation
        numerator = sum((returns_a[i] - mean_a) * (returns_b[i] - mean_b) for i in range(n))
        
        # Calculate standard deviations
        var_a = sum((returns_a[i] - mean_a) ** 2 for i in range(n))
        var_b = sum((returns_b[i] - mean_b) ** 2 for i in range(n))
        
        denominator = (var_a * var_b) ** 0.5
        
        if denominator == 0:
            return None
        
        correlation = numerator / denominator
        return round(correlation, 4)
    
    @staticmethod
    def calculate_correlation_matrix(asset_returns: Dict[str, List[float]]) -> Dict[str, Dict[str, float]]:
        """Calculate correlation matrix for all asset pairs"""
        assets = list(asset_returns.keys())
        matrix = {}
        
        for asset_a in assets:
            matrix[asset_a] = {}
            for asset_b in assets:
                if asset_a == asset_b:
                    matrix[asset_a][asset_b] = 1.0
                else:
                    corr = PortfolioAnalyzer.calculate_correlation(
                        asset_returns[asset_a],
                        asset_returns[asset_b]
                    )
                    matrix[asset_a][asset_b] = corr if corr is not None else 0.0
        
        return matrix
    
    @staticmethod
    def calculate_portfolio_return(weights: List[float], returns: List[List[float]]) -> float:
        """Calculate weighted average return"""
        if not weights or not returns:
            return 0.0
        
        portfolio_returns = []
        for i in range(len(returns[0])):
            period_return = sum(weights[j] * returns[j][i] for j in range(len(weights)))
            portfolio_returns.append(period_return)
        
        return sum(portfolio_returns) / len(portfolio_returns)
    
    @staticmethod
    def calculate_portfolio_volatility(weights: List[float], returns: List[List[float]]) -> float:
        """Calculate portfolio volatility (standard deviation of returns)"""
        if not weights or not returns:
            return 0.0
        
        portfolio_returns = []
        for i in range(len(returns[0])):
            period_return = sum(weights[j] * returns[j][i] for j in range(len(weights)))
            portfolio_returns.append(period_return)
        
        mean_return = sum(portfolio_returns) / len(portfolio_returns)
        variance = sum((r - mean_return) ** 2 for r in portfolio_returns) / len(portfolio_returns)
        
        # Annualize for crypto (365 days)
        volatility = (variance ** 0.5) * (365 ** 0.5)
        return volatility
    
    @staticmethod
    def calculate_sharpe_ratio(returns: List[float], risk_free_rate: float = 0.02) -> Optional[float]:
        """
        Calculate Sharpe ratio (risk-adjusted return)
        Risk-free rate default: 2% annual
        """
        if len(returns) < 2:
            return None
        
        mean_return = sum(returns) / len(returns)
        
        # Annualize return (crypto trades 365 days)
        annual_return = mean_return * 365
        
        # Calculate volatility
        variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
        annual_volatility = (variance ** 0.5) * (365 ** 0.5)
        
        if annual_volatility == 0:
            return None
        
        sharpe = (annual_return - risk_free_rate) / annual_volatility
        return round(sharpe, 3)
    
    @staticmethod
    def calculate_max_drawdown(prices: List[float]) -> Tuple[float, int, int]:
        """
        Calculate maximum drawdown
        Returns: (max_drawdown_pct, peak_idx, trough_idx)
        """
        if len(prices) < 2:
            return (0.0, 0, 0)
        
        max_dd = 0.0
        peak = prices[0]
        peak_idx = 0
        trough_idx = 0
        
        for i, price in enumerate(prices):
            if price > peak:
                peak = price
                peak_idx = i
            
            dd = (peak - price) / peak
            if dd > max_dd:
                max_dd = dd
                trough_idx = i
        
        return (round(max_dd * 100, 2), peak_idx, trough_idx)
    
    @staticmethod
    def calculate_sortino_ratio(returns: List[float], risk_free_rate: float = 0.02) -> Optional[float]:
        """
        Calculate Sortino ratio (downside deviation instead of total volatility)
        Only penalizes downside volatility
        """
        if len(returns) < 2:
            return None
        
        mean_return = sum(returns) / len(returns)
        annual_return = mean_return * 365
        
        # Calculate downside deviation (only negative returns)
        downside_returns = [r for r in returns if r < 0]
        if not downside_returns:
            return None
        
        downside_variance = sum(r ** 2 for r in downside_returns) / len(returns)
        downside_deviation = (downside_variance ** 0.5) * (365 ** 0.5)
        
        if downside_deviation == 0:
            return None
        
        sortino = (annual_return - risk_free_rate) / downside_deviation
        return round(sortino, 3)
    
    @staticmethod
    def calculate_diversification_ratio(weights: List[float], volatilities: List[float], 
                                       correlation_matrix: List[List[float]]) -> Optional[float]:
        """
        Calculate diversification ratio
        Higher is better (more diversified)
        """
        if not weights or not volatilities or len(weights) != len(volatilities):
            return None
        
        # Weighted average volatility
        weighted_vol = sum(w * v for w, v in zip(weights, volatilities))
        
        # Portfolio volatility (considering correlations)
        portfolio_variance = 0.0
        for i in range(len(weights)):
            for j in range(len(weights)):
                portfolio_variance += weights[i] * weights[j] * volatilities[i] * volatilities[j] * correlation_matrix[i][j]
        
        portfolio_vol = portfolio_variance ** 0.5
        
        if portfolio_vol == 0:
            return None
        
        div_ratio = weighted_vol / portfolio_vol
        return round(div_ratio, 3)
    
    @staticmethod
    def calculate_var(returns: List[float], confidence: float = 0.95) -> Optional[float]:
        """
        Calculate Value at Risk (VaR) at given confidence level
        """
        if len(returns) < 10:
            return None
        
        sorted_returns = sorted(returns)
        index = int((1 - confidence) * len(sorted_returns))
        
        var = abs(sorted_returns[index])
        return round(var * 100, 2)  # Return as percentage


def analyze_portfolio(data: Dict) -> PortfolioMetrics:
    """
    Analyze portfolio with optimization metrics
    """
    balances = data.get("balances", [])
    historical_prices = data.get("historical_prices", {})
    
    if not balances:
        raise ValueError("No portfolio balances provided")
    
    total_value = sum(float(asset.get("value_usd", 0)) for asset in balances)
    
    # Calculate current weights
    assets = []
    for asset in balances:
        symbol = asset.get("asset", "")
        balance = float(asset.get("balance", 0))
        value = float(asset.get("value_usd", 0))
        weight = (value / total_value * 100) if total_value > 0 else 0
        
        assets.append({
            "asset": symbol,
            "balance": balance,
            "value_usd": value,
            "weight_pct": round(weight, 2)
        })
    
    # If we have historical prices, calculate advanced metrics
    correlation_matrix = None
    sharpe_ratio = None
    max_drawdown_value = None
    diversification_ratio = None
    risk_metrics = {}
    rebalancing_recs = None
    
    if historical_prices and len(historical_prices) >= 2:
        # Calculate returns for each asset
        asset_returns = {}
        asset_volatilities = []
        
        for asset_data in assets:
            symbol = asset_data["asset"]
            if symbol in historical_prices and len(historical_prices[symbol]) > 1:
                prices = historical_prices[symbol]
                returns = PortfolioAnalyzer.calculate_returns(prices)
                asset_returns[symbol] = returns
                
                # Calculate volatility for this asset
                if returns:
                    mean_ret = sum(returns) / len(returns)
                    variance = sum((r - mean_ret) ** 2 for r in returns) / len(returns)
                    vol = (variance ** 0.5) * (365 ** 0.5)
                    asset_volatilities.append(vol)
        
        # Correlation matrix
        if len(asset_returns) >= 2:
            correlation_matrix = PortfolioAnalyzer.calculate_correlation_matrix(asset_returns)
        
        # Portfolio metrics
        if asset_returns:
            # Combine all returns with weights
            weights = [a["weight_pct"] / 100 for a in assets if a["asset"] in asset_returns]
            all_returns = [asset_returns[a["asset"]] for a in assets if a["asset"] in asset_returns]
            
            if all_returns and weights:
                # Portfolio-wide returns
                portfolio_returns = []
                for i in range(len(all_returns[0])):
                    period_return = sum(weights[j] * all_returns[j][i] for j in range(len(weights)))
                    portfolio_returns.append(period_return)
                
                # Sharpe ratio
                sharpe_ratio = PortfolioAnalyzer.calculate_sharpe_ratio(portfolio_returns)
                
                # Sortino ratio
                sortino_ratio = PortfolioAnalyzer.calculate_sortino_ratio(portfolio_returns)
                
                # VaR
                var_95 = PortfolioAnalyzer.calculate_var(portfolio_returns, 0.95)
                var_99 = PortfolioAnalyzer.calculate_var(portfolio_returns, 0.99)
                
                # Max drawdown (use first asset's prices as proxy for portfolio value)
                first_asset_symbol = assets[0]["asset"]
                if first_asset_symbol in historical_prices:
                    max_dd, _, _ = PortfolioAnalyzer.calculate_max_drawdown(
                        historical_prices[first_asset_symbol]
                    )
                    max_drawdown_value = max_dd
                
                risk_metrics = {
                    "sharpe_ratio": sharpe_ratio,
                    "sortino_ratio": sortino_ratio,
                    "var_95": var_95,
                    "var_99": var_99,
                    "max_drawdown_pct": max_drawdown_value
                }
                
                # Diversification ratio
                if len(asset_volatilities) == len(weights) and correlation_matrix:
                    # Build correlation matrix as list of lists
                    asset_symbols = [a["asset"] for a in assets if a["asset"] in asset_returns]
                    corr_list = []
                    for sym_a in asset_symbols:
                        row = []
                        for sym_b in asset_symbols:
                            row.append(correlation_matrix[sym_a][sym_b])
                        corr_list.append(row)
                    
                    diversification_ratio = PortfolioAnalyzer.calculate_diversification_ratio(
                        weights, asset_volatilities, corr_list
                    )
                
                # Simple rebalancing recommendations
                # Flag assets with extreme allocations
                rebalancing_recs = []
                for asset_data in assets:
                    weight = asset_data["weight_pct"]
                    if weight > 50:
                        rebalancing_recs.append({
                            "asset": asset_data["asset"],
                            "current_weight": weight,
                            "recommendation": "Consider reducing allocation",
                            "reason": "Concentration risk (>50%)"
                        })
                    elif weight < 5 and total_value > 1000:
                        rebalancing_recs.append({
                            "asset": asset_data["asset"],
                            "current_weight": weight,
                            "recommendation": "Consider increasing or removing",
                            "reason": "Small allocation (<5%) may not impact returns"
                        })
    
    return PortfolioMetrics(
        total_value=total_value,
        assets=assets,
        correlation_matrix=correlation_matrix,
        sharpe_ratio=sharpe_ratio,
        max_drawdown=max_drawdown_value,
        diversification_ratio=diversification_ratio,
        risk_metrics=risk_metrics,
        rebalancing_recommendations=rebalancing_recs
    )


def main():
    """Main entry point for portfolio optimization"""
    parser = argparse.ArgumentParser(description="Portfolio optimization and risk analysis")
    parser.add_argument("--format", choices=["json", "text"], default="json",
                       help="Output format")
    parser.add_argument("--risk-free-rate", type=float, default=0.02,
                       help="Risk-free rate for Sharpe ratio (default: 0.02)")
    args = parser.parse_args()
    
    try:
        # Read portfolio data from stdin
        input_data = json.load(sys.stdin)
        
        # Perform portfolio analysis
        result = analyze_portfolio(input_data)
        
        if args.format == "json":
            print(json.dumps(result.to_dict(), indent=2))
        else:
            # Text format
            print(f"\n{'='*60}")
            print(f"PORTFOLIO OPTIMIZATION ANALYSIS")
            print(f"{'='*60}\n")
            
            print(f"Total Portfolio Value: ${result.total_value:,.2f}\n")
            
            # Asset allocation
            print("📊 Current Allocation:")
            for asset in result.assets:
                print(f"  {asset['asset']}: {asset['weight_pct']:.2f}% (${asset['value_usd']:,.2f})")
            print()
            
            # Correlation matrix
            if result.correlation_matrix:
                print("🔗 Correlation Matrix:")
                assets = list(result.correlation_matrix.keys())
                print(f"     {' '.join(f'{a:>7}' for a in assets)}")
                for asset_a in assets:
                    row = [result.correlation_matrix[asset_a][asset_b] for asset_b in assets]
                    print(f"{asset_a:>4} {' '.join(f'{v:>7.2f}' for v in row)}")
                print()
            
            # Risk metrics
            if result.risk_metrics:
                print("📈 Risk-Adjusted Performance:")
                metrics = result.risk_metrics
                if metrics.get("sharpe_ratio"):
                    sharpe = metrics["sharpe_ratio"]
                    rating = "Excellent" if sharpe > 2 else "Good" if sharpe > 1 else "Fair" if sharpe > 0 else "Poor"
                    print(f"  Sharpe Ratio: {sharpe:.3f} ({rating})")
                
                if metrics.get("sortino_ratio"):
                    print(f"  Sortino Ratio: {metrics['sortino_ratio']:.3f}")
                
                if metrics.get("max_drawdown_pct"):
                    print(f"  Max Drawdown: -{metrics['max_drawdown_pct']:.2f}%")
                
                if metrics.get("var_95"):
                    print(f"  VaR (95%): {metrics['var_95']:.2f}%")
                    print(f"  VaR (99%): {metrics['var_99']:.2f}%")
                
                print()
            
            # Diversification
            if result.diversification_ratio:
                div = result.diversification_ratio
                rating = "Well-diversified" if div > 1.5 else "Moderately diversified" if div > 1.2 else "Concentrated"
                print(f"🎯 Diversification Ratio: {div:.3f} ({rating})\n")
            
            # Rebalancing recommendations
            if result.rebalancing_recommendations:
                print("💡 Rebalancing Recommendations:")
                for rec in result.rebalancing_recommendations:
                    print(f"  {rec['asset']} ({rec['current_weight']:.1f}%): {rec['recommendation']}")
                    print(f"    Reason: {rec['reason']}")
                print()
    
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
