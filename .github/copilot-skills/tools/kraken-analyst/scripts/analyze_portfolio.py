#!/usr/bin/env python3
"""
analyze_portfolio.py - Kraken Analyst Skill: Portfolio Analysis Module

Analyzes portfolio data and provides allocation recommendations.
Takes portfolio JSON from stdin (from fetch_portfolio.py).

Outputs deterministic JSON to stdout with analysis and recommendations.

Usage:
    python fetch_portfolio.py --portfolio-summary | python analyze_portfolio.py
    python fetch_portfolio.py --portfolio-summary | python analyze_portfolio.py --target-allocation portfolio.json

Outputs:
    JSON with portfolio analysis, risk metrics, and rebalancing recommendations
"""

import json
import sys
import argparse
from typing import Dict, List, Optional


class PortfolioAnalyzer:
    """Analyzes crypto portfolio allocation and risk"""
    
    # Default target allocations for different risk profiles
    DEFAULT_TARGETS = {
        "conservative": {
            "BTC": 40,
            "ETH": 20,
            "stablecoins": 40
        },
        "moderate": {
            "BTC": 50,
            "ETH": 25,
            "alts": 10,
            "stablecoins": 15
        },
        "aggressive": {
            "BTC": 55,
            "ETH": 25,
            "alts": 15,
            "stablecoins": 5
        },
        "medium-high": {
            "BTC": 55,
            "ETH": 20,
            "alts": 10,
            "stablecoins": 15
        }
    }
    
    STABLECOINS = ["ZUSD", "USD", "USDC", "USDT", "DAI", "PYUSD"]
    MAJOR_ALTS = ["SOL", "ADA", "DOT", "LINK", "MATIC", "AVAX", "XRP"]
    
    def __init__(self, target_allocation: Optional[Dict] = None, risk_profile: str = "medium-high"):
        """
        Initialize analyzer
        
        Args:
            target_allocation: Custom target allocation (optional)
            risk_profile: Risk profile name (conservative/moderate/aggressive/medium-high)
        """
        self.target_allocation = target_allocation or self.DEFAULT_TARGETS.get(risk_profile, self.DEFAULT_TARGETS["medium-high"])
        self.risk_profile = risk_profile
    
    def classify_asset(self, asset: str) -> str:
        """
        Classify asset into category
        
        Args:
            asset: Asset symbol (e.g., "XXBT", "XETH", "SOL")
            
        Returns:
            Category: "BTC", "ETH", "alts", "stablecoins"
        """
        # Remove X/Z prefix for comparison
        clean_asset = asset.replace("X", "").replace("Z", "")
        
        if clean_asset in ["BTC", "XBT"]:
            return "BTC"
        elif clean_asset == "ETH":
            return "ETH"
        elif asset in self.STABLECOINS or clean_asset in self.STABLECOINS:
            return "stablecoins"
        elif clean_asset in self.MAJOR_ALTS:
            return "alts"
        else:
            return "alts"  # Default to alts
    
    def analyze_allocation(self, portfolio: List[Dict]) -> Dict:
        """
        Analyze portfolio allocation vs targets
        
        Args:
            portfolio: List of portfolio items with asset, amount, value_usd, weight
            
        Returns:
            Analysis with current allocation, drift from targets, and recommendations
        """
        # Calculate current allocation by category
        current_allocation = {
            "BTC": 0.0,
            "ETH": 0.0,
            "alts": 0.0,
            "stablecoins": 0.0
        }
        
        total_value = 0.0
        asset_details = []
        
        for item in portfolio:
            category = self.classify_asset(item["asset"])
            current_allocation[category] += item["weight"]
            total_value += item["value_usd"]
            
            asset_details.append({
                "asset": item["asset"],
                "category": category,
                "amount": item["amount"],
                "value_usd": item["value_usd"],
                "weight": item["weight"]
            })
        
        # Calculate drift from targets
        drift = {}
        for category, target_weight in self.target_allocation.items():
            current_weight = current_allocation.get(category, 0.0)
            drift[category] = current_weight - target_weight
        
        # Identify assets that need rebalancing (>10% drift)
        rebalancing_needed = any(abs(d) > 10 for d in drift.values())
        
        # Generate recommendations
        recommendations = []
        
        for category, drift_pct in drift.items():
            if abs(drift_pct) > 10:
                if drift_pct > 0:
                    action = "REDUCE"
                    amount_usd = (drift_pct / 100) * total_value
                    recommendations.append({
                        "category": category,
                        "action": action,
                        "current_weight": current_allocation.get(category, 0.0),
                        "target_weight": self.target_allocation[category],
                        "drift_pct": drift_pct,
                        "amount_usd": amount_usd,
                        "priority": "HIGH" if abs(drift_pct) > 15 else "MEDIUM"
                    })
                else:
                    action = "INCREASE"
                    amount_usd = (abs(drift_pct) / 100) * total_value
                    recommendations.append({
                        "category": category,
                        "action": action,
                        "current_weight": current_allocation.get(category, 0.0),
                        "target_weight": self.target_allocation[category],
                        "drift_pct": drift_pct,
                        "amount_usd": amount_usd,
                        "priority": "HIGH" if abs(drift_pct) > 15 else "MEDIUM"
                    })
        
        return {
            "total_value_usd": total_value,
            "current_allocation": current_allocation,
            "target_allocation": self.target_allocation,
            "drift": drift,
            "rebalancing_needed": rebalancing_needed,
            "recommendations": recommendations,
            "asset_details": asset_details
        }
    
    def calculate_risk_metrics(self, portfolio: List[Dict], allocation_analysis: Dict) -> Dict:
        """
        Calculate portfolio risk metrics
        
        Args:
            portfolio: Portfolio items
            allocation_analysis: Allocation analysis results
            
        Returns:
            Risk metrics
        """
        # Concentration risk (Herfindahl-Hirschman Index)
        hhi = sum((item["weight"] / 100) ** 2 for item in portfolio)
        
        # Diversification score (0-100, higher is better)
        diversification_score = (1 - hhi) * 100
        
        # Stablecoin buffer adequacy
        stable_weight = allocation_analysis["current_allocation"].get("stablecoins", 0.0)
        buffer_status = "ADEQUATE" if stable_weight >= 15 else "LOW" if stable_weight >= 5 else "CRITICAL"
        
        # Volatility exposure (weighted by allocation)
        # Rough volatility estimates
        volatility_weights = {
            "BTC": 60,
            "ETH": 75,
            "alts": 90,
            "stablecoins": 0
        }
        
        portfolio_volatility = sum(
            allocation_analysis["current_allocation"].get(cat, 0) * vol / 100
            for cat, vol in volatility_weights.items()
        )
        
        return {
            "concentration_index": hhi,
            "diversification_score": diversification_score,
            "stablecoin_buffer": stable_weight,
            "buffer_status": buffer_status,
            "estimated_volatility": portfolio_volatility,
            "risk_level": "HIGH" if portfolio_volatility > 70 else "MEDIUM" if portfolio_volatility > 50 else "LOW"
        }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze portfolio allocation and generate recommendations",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--risk-profile",
        choices=["conservative", "moderate", "aggressive", "medium-high"],
        default="medium-high",
        help="Risk profile for target allocation"
    )
    
    parser.add_argument(
        "--target-allocation",
        type=str,
        help="Path to JSON file with custom target allocation"
    )
    
    parser.add_argument(
        "--format",
        choices=["json", "pretty"],
        default="json",
        help="Output format"
    )
    
    args = parser.parse_args()
    
    # Read portfolio data from stdin
    try:
        portfolio_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Load custom target allocation if provided
    target_allocation = None
    if args.target_allocation:
        try:
            with open(args.target_allocation, 'r') as f:
                target_allocation = json.load(f)
        except Exception as e:
            print(f"ERROR: Failed to load target allocation: {e}", file=sys.stderr)
            sys.exit(1)
    
    # Initialize analyzer
    analyzer = PortfolioAnalyzer(
        target_allocation=target_allocation,
        risk_profile=args.risk_profile
    )
    
    # Extract portfolio from input
    portfolio = portfolio_data.get("portfolio", [])
    if not portfolio:
        print("ERROR: No portfolio data in input", file=sys.stderr)
        sys.exit(1)
    
    # Analyze allocation
    allocation_analysis = analyzer.analyze_allocation(portfolio)
    
    # Calculate risk metrics
    risk_metrics = analyzer.calculate_risk_metrics(portfolio, allocation_analysis)
    
    # Compile results
    result = {
        "timestamp": portfolio_data.get("timestamp"),
        "risk_profile": args.risk_profile,
        "allocation_analysis": allocation_analysis,
        "risk_metrics": risk_metrics
    }
    
    # Output
    if args.format == "pretty":
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))


if __name__ == "__main__":
    main()
