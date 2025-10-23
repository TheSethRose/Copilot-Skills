---
name: kraken-analyst
description: Professional-grade crypto analysis with advanced technical indicators, portfolio optimization, and risk metrics.
version: "2.0.0"
tags: ["crypto", "market", "kraken", "strategy", "analysis", "technical-indicators", "portfolio-optimization"]
dependencies: ["python3"]
license: MIT
---

# Kraken Analyst Copilot Skill

A professional quantitative analysis skill for cryptocurrency markets featuring advanced technical indicators, Modern Portfolio Theory optimization, and comprehensive risk metrics. Built using official Kraken API documentation with patterns extracted from MaverickMCP.

## Overview

The Kraken Analyst skill provides:

- **Live Data Fetching** - Real-time OHLC data from Kraken REST API v0
- **Advanced Technical Analysis** - 20+ indicators including Ichimoku, ATR, Stochastic RSI, support/resistance detection
- **Portfolio Optimization** - Modern Portfolio Theory with correlation matrix, Sharpe ratio, diversification metrics
- **Quantitative Signals** - BUY, SELL, HOLD recommendations with confidence scoring
- **Risk Management** - Maximum drawdown, VaR, Sortino ratio, volatility analysis
- **Structured Output** - JSON + Markdown formatted reports
- **Portfolio Management** - Account balance tracking, allocation analysis, and rebalancing (requires API keys)

## Quick Start

### Public Endpoints (No API Keys Required)

> **Note**: Market analysis features use **public Kraken API endpoints** and do NOT require API keys or authentication. You can use them immediately without any setup!

### Private Endpoints (API Keys Required)

> **Note**: Portfolio management features require **Kraken API credentials**. See [Authentication Setup](#authentication-setup) below.

### 1. Fetch Market Data

```bash
python .github/copilot-skills/tools/kraken-analyst/scripts/fetch_data.py \
  --pair BTC/USD \
  --interval 60 \
  --count 100
```

### 2. Apply Analysis Rules

```bash
python .github/copilot-skills/tools/kraken-analyst/scripts/fetch_data.py --pair BTC/USD | \
python .github/copilot-skills/tools/kraken-analyst/scripts/apply_rules.py
```

### 3. Generate Report

```bash
python .github/copilot-skills/tools/kraken-analyst/scripts/fetch_data.py --pair ETH/USD | \
python .github/copilot-skills/tools/kraken-analyst/scripts/apply_rules.py | \
python .github/copilot-skills/tools/kraken-analyst/scripts/format_output.py
```

### Complete Pipeline

```bash
# Full analysis with markdown report
python .github/copilot-skills/tools/kraken-analyst/scripts/fetch_data.py --pair BTC/USD --interval 60 --count 100 | \
python .github/copilot-skills/tools/kraken-analyst/scripts/apply_rules.py | \
python .github/copilot-skills/tools/kraken-analyst/scripts/format_output.py --format markdown --include-charts
```

## Scripts

### fetch_data.py

Fetches OHLC candle data from Kraken REST API.

**API Endpoint**: `GET https://api.kraken.com/0/public/OHLC`

**Usage:**
```bash
python fetch_data.py --pair BTC/USD --interval 60 --count 100
python fetch_data.py --pair XXBTZUSD --interval 1440 --count 30
python fetch_data.py --list-pairs
```

**Parameters:**
- `--pair` - Trading pair (BTC/USD, ETH/EUR, or Kraken format XXBTZUSD)
- `--interval` - Candle interval in minutes: 1, 5, 15, 30, 60, 240, 1440, 10080, 21600
- `--count` - Number of candles to fetch (1-720, default: 100)
- `--rate-limit` - Seconds between API requests (default: 0.5)
- `--list-pairs` - List all supported trading pairs
- `--list-intervals` - List all supported intervals

**Output:**
```json
{
  "pair": "BTC/USD",
  "pair_kraken": "XXBTZUSD",
  "interval": 60,
  "interval_name": "1h",
  "data_points": 100,
  "timestamp": "2025-10-20T02:45:00.000Z",
  "source": "Kraken REST API v0",
  "data": [
    {
      "timestamp": 1697750400,
      "datetime": "2023-10-20T02:00:00",
      "open": 27500.0,
      "high": 27650.5,
      "low": 27400.0,
      "close": 27600.0,
      "vwap": 27550.0,
      "volume": 125.5,
      "count": 150
    }
  ]
}
```

### apply_rules.py

Applies momentum, volatility, and trend analysis rules.

**Usage:**
```bash
python apply_rules.py < market_data.json
python apply_rules.py --momentum-threshold 1.5 --volatility-threshold 3.0 < data.json
```

**Parameters:**
- `--momentum-threshold` - Std deviations for momentum signal (default: 2.0)
- `--volatility-threshold` - Annualized volatility threshold % (default: 2.5)
- `--rsi-period` - RSI calculation period (default: 14)
- `--ma-fast` - Fast moving average period (default: 12)
- `--ma-slow` - Slow moving average period (default: 26)

**Output:**
```json
{
  "pair": "BTC/USD",
  "timestamp": 1697750400,
  "current_price": 27600.0,
  "analysis": {
    "momentum": 2.4,
    "momentum_threshold": 2.0,
    "volatility": 1.8,
    "volatility_threshold": 2.5,
    "rsi": 65.2,
    "rsi_period": 14,
    "ma_fast": 27550.0,
    "ma_slow": 27450.0,
    "ma_signal": "bullish",
    "price_change_pct": 0.36,
    "recent_volume": 125.5,
    "avg_volume": 100.0,
    "volume_ratio": 1.26
  },
  "signal": "BUY",
  "confidence": 0.820
}
```

### format_output.py

Generates human-readable analysis reports.

**Usage:**
```bash
python format_output.py < analysis.json
python format_output.py --format markdown --include-charts < analysis.json
python format_output.py --format text < analysis.json
```

**Parameters:**
- `--format` - Output format: `markdown`, `json`, `text` (default: markdown)
- `--include-charts` - Generate ASCII charts (default: false)

**Output (Markdown):**
```markdown
# Kraken Analysis Report

## BTC/USD Analysis
- **Signal**: BUY ⬆️ 📈
- **Confidence**: 82.0%
- **Current Price**: $27,600.00
- **Timestamp**: 2023-10-20 02:00:00 UTC

### Technical Indicators
| Indicator | Value | Interpretation |
|-----------|-------|----------------|
| **Momentum** | 2.40σ | Strong upward momentum 🚀 |
| **Volatility** | 1.80% | Normal volatility ✅ |
| **RSI** | 65.2 | Strong |
...
```

## Portfolio Management (Private API)

### Authentication Setup

To use portfolio management features, you need Kraken API credentials with appropriate permissions.

**📋 DETAILED PERMISSIONS GUIDE**: See [`PERMISSIONS.md`](./PERMISSIONS.md) for complete guidance on:
- Which permissions each feature needs
- Security recommendations (IP restriction, key expiration)
- Step-by-step API key creation instructions
- Troubleshooting permission errors

**Quick Setup for Portfolio View (Minimum)**:

1. **Login to Kraken**: https://www.kraken.com
2. **Go to Settings → API**
3. **Create New API Key** with ONLY these permissions:
   - ✅ **Funds → Query** (for viewing balances)
   - ❌ Leave all others unchecked
4. **Enable Security Settings**:
   - ✅ IP Address Restriction: Add your IP
   - ✅ Key Expiration: Set to 90 days
5. **Copy credentials**:
   ```bash
   cp .github/copilot-skills/tools/kraken-analyst/.env.example \
      .github/copilot-skills/tools/kraken-analyst/.env
   
   # Edit .env and add your credentials:
   # KRAKEN_API_KEY=your-api-key-here
   # KRAKEN_PRIVATE_KEY=your-private-key-here
   ```
6. **Test**:
   ```bash
   python fetch_portfolio.py --balances
   ```

**For Full Analysis** (with trade history), see [`PERMISSIONS.md`](./PERMISSIONS.md) for additional permissions needed.

**Security Best Practices:**
- ✅ Never commit `.env` file to git (already in `.gitignore`)
- ✅ Grant **only minimum required permissions** for your use case
- ✅ Always enable **IP whitelisting**
- ✅ Set **key expiration** (30-90 days)
- ✅ Rotate keys regularly
- ✅ Never grant: Create/Cancel Orders, Withdraw, Deposit
- ✅ Monitor API key usage in Kraken dashboard

### kraken_auth.py

Authentication helper for private endpoints.

**Usage:**
```bash
# Test authentication
python kraken_auth.py
```

**Output:**
```
✓ API credentials configured
Testing connection...
✓ Authentication successful
{
  "XXBT": "0.12345678",
  "ZEUR": "1234.56",
  ...
}
```

### fetch_portfolio.py

Fetches account portfolio data from private API endpoints including **Kraken Earn (staking)** allocations.

**Requires**: API credentials in `.env` file (auto-loaded, no manual sourcing needed!)

**Features**:
- ✅ Fetches spot balances
- ✅ Fetches Kraken Earn (staking) allocations with APR
- ✅ Combines spot + earn for total portfolio value
- ✅ Maps futures/spread contracts to spot prices
- ✅ Calculates allocation percentages
- ✅ Real-time USD values from Kraken Ticker API

**Usage:**
```bash
# Get account balances (spot + futures/spreads)
python3 fetch_portfolio.py --balances

# Get complete portfolio summary (spot + Kraken Earn staking)
python3 fetch_portfolio.py --portfolio-summary --format pretty

# Get open orders
python3 fetch_portfolio.py --open-orders

# Get recent trade history
python fetch_portfolio.py --trade-history --count 20

# Get trade volume and fees
python fetch_portfolio.py --trade-volume
```

**Parameters:**
- `--balances` - Fetch account balances
- `--portfolio-summary` - Fetch complete portfolio with USD valuations
- `--open-orders` - Fetch open orders
- `--trade-history` - Fetch trade history
- `--trade-volume` - Fetch volume and fee information
- `--count` - Number of items (for trade history, default: 10)
- `--format` - Output format: `json` or `pretty` (default: json)

**Output (Portfolio Summary):**
```json
{
  "timestamp": 1761191977.861,
  "total_value_usd": 373.87,
  "spot_value_usd": 0.02,
  "earn_value_usd": 373.85,
  "spot_portfolio": [
    {
      "asset": "ZUSD",
      "amount": 0.0098,
      "price_usd": 1.0,
      "value_usd": 0.0098,
      "weight": 53.95
    },
    {
      "asset": "BABY",
      "amount": 0.27133,
      "price_usd": 0.03083,
      "value_usd": 0.0084,
      "weight": 46.05
    }
  ],
  "earn_allocations": [
    {
      "asset": "BTC",
      "amount": 0.00240970,
      "price_usd": 108400.0,
      "value_usd": 261.19,
      "strategy": "ESPR2DI-WN476-TBRFLO",
      "apr": 0.5
    },
    {
      "asset": "SOL",
      "amount": 0.25000000,
      "price_usd": 182.82,
      "value_usd": 45.71,
      "strategy": "ES4TNKS-MWG4P-Y3GIRT",
      "apr": 3.2
    },
    {
      "asset": "SOL",
      "amount": 0.45,
      "price_usd": 187.06,
      "value_usd": 84.18,
      "weight": 22.29
    },
    ...
  ]
}
```

### analyze_portfolio.py

Analyzes portfolio allocation and provides rebalancing recommendations.

**Usage:**
```bash
# Analyze with default risk profile (medium-high)
python fetch_portfolio.py --portfolio-summary | python analyze_portfolio.py

# Analyze with specific risk profile
python fetch_portfolio.py --portfolio-summary | \
python analyze_portfolio.py --risk-profile aggressive

# Analyze with custom target allocation
python fetch_portfolio.py --portfolio-summary | \
python analyze_portfolio.py --target-allocation my_targets.json
```

**Parameters:**
- `--risk-profile` - Risk profile: `conservative`, `moderate`, `aggressive`, `medium-high` (default)
- `--target-allocation` - Path to JSON file with custom targets
- `--format` - Output format: `json` or `pretty`

**Risk Profiles:**

| Profile | BTC | ETH | Alts | Stablecoins |
|---------|-----|-----|------|-------------|
| **Conservative** | 40% | 20% | 0% | 40% |
| **Moderate** | 50% | 25% | 10% | 15% |
| **Aggressive** | 55% | 25% | 15% | 5% |
| **Medium-High** | 55% | 20% | 10% | 15% |

**Output:**
```json
{
  "timestamp": 1697834523.456,
  "risk_profile": "medium-high",
  "allocation_analysis": {
    "total_value_usd": 377.69,
    "current_allocation": {
      "BTC": 69.46,
      "ETH": 2.72,
      "alts": 27.82,
      "stablecoins": 0.0
    },
    "target_allocation": {
      "BTC": 55,
      "ETH": 20,
      "alts": 10,
      "stablecoins": 15
    },
    "drift": {
      "BTC": 14.46,
      "ETH": -17.28,
      "alts": 17.82,
      "stablecoins": -15.0
    },
    "rebalancing_needed": true,
    "recommendations": [
      {
        "category": "BTC",
        "action": "REDUCE",
        "current_weight": 69.46,
        "target_weight": 55,
        "drift_pct": 14.46,
        "amount_usd": 54.63,
        "priority": "MEDIUM"
      },
      {
        "category": "ETH",
        "action": "INCREASE",
        "current_weight": 2.72,
        "target_weight": 20,
        "drift_pct": -17.28,
        "amount_usd": 65.26,
        "priority": "HIGH"
      },
      ...
    ]
  },
  "risk_metrics": {
    "concentration_index": 0.562,
    "diversification_score": 43.8,
    "stablecoin_buffer": 0.0,
    "buffer_status": "CRITICAL",
    "estimated_volatility": 72.4,
    "risk_level": "HIGH"
  }
}
```

### Complete Portfolio Workflow

```bash
# 1. Check account balances
python fetch_portfolio.py --balances --format pretty

# 2. Get portfolio summary with USD values
python fetch_portfolio.py --portfolio-summary --format pretty

# 3. Analyze allocation and get recommendations
python fetch_portfolio.py --portfolio-summary | \
python analyze_portfolio.py --risk-profile medium-high --format pretty

# 4. Save analysis to file
python fetch_portfolio.py --portfolio-summary | \
python analyze_portfolio.py > portfolio_analysis.json
```

## Portfolio Tracking & Historical Analysis (NEW)

Track your portfolio performance over time, log recommendations, and measure actual results against recommendations.

### Database Setup

The skill includes a SQLite database for tracking:
- Historical portfolio snapshots (balances over time)
- Technical analysis signals (logged automatically)
- Recommendations with confidence scores
- Recommendation outcomes (actual vs target)
- Performance metrics (returns, accuracy, ROI)

**Initialize Database** (one-time setup):
```bash
cd .github/copilot-skills/tools/kraken-analyst/scripts
python3 db_init.py
```

**Output:**
```
✅ Database initialization complete!
✓ All verification checks passed!
```

### track_portfolio.py

Save portfolio snapshots to track allocation and value changes over time.

**Usage:**
```bash
# Save current portfolio snapshot
python3 track_portfolio.py

# View portfolio history (last 30 days)
python3 track_portfolio.py --history 30

# Compare to previous snapshot
python3 track_portfolio.py --compare

# Export to CSV
python3 track_portfolio.py --csv
```

**Output Example:**
```
✓ Portfolio snapshot saved
  Timestamp: 2025-10-23T04:28:16.792700
  Total Value: $374.80
  Holdings: 2 spot + 6 earn

Portfolio History (Last 30 days)
========================================
Timestamp              Total Value    Spot       Earn
2025-10-23 04:28      $374.80       $0.02      $374.78
```

**Features:**
- ✅ Automatic timestamp recording
- ✅ Tracks spot + earn balances
- ✅ Historical comparisons
- ✅ CSV export for analysis
- ✅ Per-asset value tracking

### log_recommendations.py

Log investment recommendations with confidence scores and track how they perform.

**Usage:**
```bash
# Log a recommendation
python3 log_recommendations.py --log DOT SELL 2.92 3.15 0.65 "Exit 50% on bounce"

# Review recent recommendations
python3 log_recommendations.py --review

# Review specific asset recommendations
python3 log_recommendations.py --review --asset BTC --days 30

# Calculate recommendation accuracy
python3 log_recommendations.py --accuracy

# Mark recommendation as executed
python3 log_recommendations.py --executed 1 3.20
```

**Command Format:**
```bash
python3 log_recommendations.py --log ASSET ACTION CURRENT TARGET [CONFIDENCE] [REASON]
```

**Parameters:**
- `ASSET` - Cryptocurrency symbol (BTC, ETH, SOL, DOT)
- `ACTION` - BUY, SELL, HOLD, or REDUCE
- `CURRENT` - Current price in USD
- `TARGET` - Target price for this recommendation
- `CONFIDENCE` - Confidence score 0.0-1.0 (optional, default: 0.5)
- `REASON` - Why this recommendation (optional)

**Example Workflow:**
```bash
# Log your recommendations from analysis
python3 log_recommendations.py --log DOT SELL 2.92 3.15 0.65 "Exit 50% on bounce"
python3 log_recommendations.py --log BTC SELL 108440 112000 0.75 "Trim 20% on rally"
python3 log_recommendations.py --log SOL BUY 182.92 170 0.80 "Add on dips"
python3 log_recommendations.py --log ETH BUY 3824.07 3500 0.70 "Increase position"

# Check your recommendations
python3 log_recommendations.py --review

# When trade is executed, mark it
python3 log_recommendations.py --executed 1 3.18
python3 log_recommendations.py --executed 2 111500

# Check accuracy
python3 log_recommendations.py --accuracy
```

**Output:**
```
📋 Recommendations (Last 30 days)
========================================
ID   Date         Asset  Action  Current     Target      Conf
1    2025-10-23   DOT    SELL    $2.92       $3.15       0.65
     └─ Exit 50% on bounce to reduce concentration risk
2    2025-10-23   BTC    SELL    $108440     $112000     0.75
     └─ Trim 20% on rally to lock in gains
3    2025-10-23   SOL    BUY     $182.92     $170.00     0.80
     └─ Add 20-30% on dips to improve allocation
4    2025-10-23   ETH    BUY     $3824.07    $3500.00    0.70
     └─ Increase from 2.7% to 5% allocation on dips
```

### analyze_performance.py

Analyze how your portfolio is performing vs recommendations and market conditions.

**Usage:**
```bash
# Full performance report
python3 analyze_performance.py --report

# Analyze per-asset performance
python3 analyze_performance.py --assets

# Compare recommendations to actual results
python3 analyze_performance.py --comparison

# Show portfolio trends
python3 analyze_performance.py --trends
```

**Output Example:**
```
================================================================================
                    PORTFOLIO PERFORMANCE ANALYSIS
================================================================================

📈 90-Day Returns
----------------------------------------
Start Value:  $374.80
End Value:    $380.25
Total Return: $5.45
% Return:     1.45%

🪙 Per-Asset Performance
------------------------------------------------------------
Asset    Start Value     End Value      Return %
------------------------------------------------------------
BTC      $261.69        $265.42        +1.43%
SOL      $83.15         $87.30         +5.00%
DOT      $19.53         $18.50         -5.27%
ETH      $10.03         $10.60         +5.68%

🎯 Recommendation Accuracy
----------------------------------------
Total Recommendations: 4
Executed:              2
Met Target:            1
Accuracy Rate:         50.0%

By Asset:
  DOT      1 recs,    0.0% accuracy
  BTC      1 recs,  100.0% accuracy
  SOL      1 recs,    0.0% accuracy
  ETH      1 recs,    0.0% accuracy
```

**Metrics Tracked:**
- ✅ Total portfolio value
- ✅ Per-asset returns
- ✅ Recommendation accuracy
- ✅ Target hit rate
- ✅ Best/worst performing recommendations
- ✅ Confidence vs actual accuracy

### Complete Tracking Workflow

```bash
#!/bin/bash
# Daily portfolio tracking workflow

cd .github/copilot-skills/tools/kraken-analyst/scripts

# 1. Save current portfolio state
echo "📊 Saving portfolio snapshot..."
python3 track_portfolio.py

# 2. Review existing recommendations
echo "📋 Reviewing recommendations..."
python3 log_recommendations.py --review

# 3. Check performance
echo "📈 Analyzing performance..."
python3 analyze_performance.py --report

# 4. Export data
echo "📁 Exporting history..."
python3 track_portfolio.py --csv

echo "✅ Daily tracking complete!"
```

**Set Up Cron Job** (Automatic daily tracking):
```bash
# Edit crontab
crontab -e

# Add this line to run daily at 9 AM:
0 9 * * * cd /Users/sethrose/Developer/Tests/copilot-skills/.github/copilot-skills/tools/kraken-analyst/scripts && python3 track_portfolio.py

# Verify cron is setup
crontab -l
```

### Database Schema

The portfolio tracker uses 8 tables:

| Table | Purpose |
|-------|---------|
| `portfolio_snapshots` | Daily portfolio value snapshots |
| `asset_holdings` | Per-asset holdings at each snapshot |
| `recommendations` | All logged recommendations |
| `recommendation_outcomes` | Execution results for recommendations |
| `technical_analysis` | Technical indicators history |
| `price_history` | Historical price data |
| `performance_metrics` | Quarterly/monthly performance reports |
| `analysis_sessions` | Analysis run history |

**Accessing the Database** (Direct SQL):
```bash
# Open SQLite shell
sqlite3 portfolio_tracker.db

# List all snapshots
SELECT * FROM portfolio_snapshots;

# View recent recommendations
SELECT * FROM recommendations ORDER BY timestamp DESC LIMIT 10;

# Get portfolio growth over time
SELECT timestamp, total_value_usd FROM portfolio_snapshots ORDER BY timestamp;
```

### Database Location

Database file: `.github/copilot-skills/tools/kraken-analyst/portfolio_tracker.db`

**Important**: 
- ✅ Already added to `.gitignore` (won't be committed)
- ✅ Stored locally (your private data)
- ✅ Never uploaded to repositories
- ⚠️  Keep backups if data is important

---

## Advanced Technical Analysis (NEW)


Advanced technical indicators extracted from MaverickMCP patterns. Works with existing Kraken data without requiring additional API keys.

**Features:**
- 📊 Support & Resistance level detection
- 📈 ATR (Average True Range) for volatility measurement
- 🎯 Stochastic RSI for refined momentum signals
- 📉 EMA & WMA moving averages
- ☁️  Ichimoku Cloud for all-in-one trend analysis
- ⚠️  Divergence detection (price vs indicators)

**Usage:**
```bash
# Advanced analysis on BTC
python fetch_data.py --pair BTC/USD --interval 60 --count 100 | \
python advanced_analysis.py --format text

# JSON output for programmatic use
python fetch_data.py --pair ETH/USD | python advanced_analysis.py

# Combined with basic analysis
python fetch_data.py --pair SOL/USD | \
python apply_rules.py | \
python advanced_analysis.py
```

**Output Example:**
```
============================================================
ADVANCED TECHNICAL ANALYSIS: BTC/USD
============================================================

Current Price: $108,725.90
Timestamp: 1729582800

📊 Support & Resistance:
  Nearest Support: $106,500.00 (2.05% away)
  Nearest Resistance: $110,200.00 (1.36% away)

📈 ATR (Volatility): $2,450.00 (2.25%)

🎯 Stochastic RSI:
  %K: 65.42
  %D: 62.18
  Signal: NEUTRAL

☁️  Ichimoku Cloud:
  Tenkan-sen: $108,450.00
  Kijun-sen: $107,800.00
  Cloud: BULLISH
  Price vs Cloud: ABOVE
  Signal: STRONG_BULLISH

🚨 Advanced Signals:
  • Near Resistance Rejection Risk
  • Low Volatility Consolidation
  • Ichimoku Strong Bullish

⚠️  Divergences Detected:
  • Bullish Rsi Divergence
```

**Indicators Included:**

| Indicator | Purpose | Typical Use |
|-----------|---------|-------------|
| **Support/Resistance** | Key price levels | Entry/exit points |
| **ATR** | Volatility measurement | Position sizing |
| **Stochastic RSI** | Momentum oscillator | Overbought/oversold |
| **EMA** | Exponential moving avg | Trend confirmation |
| **WMA** | Weighted moving avg | Recent price emphasis |
| **Ichimoku Cloud** | All-in-one indicator | Trend + support/resistance |
| **Divergences** | Price vs indicator | Potential reversals |

### portfolio_optimizer.py

Modern Portfolio Theory analysis for crypto portfolios. Provides correlation analysis, Sharpe ratio optimization, and risk metrics.

**Features:**
- 🔗 Correlation matrix between holdings
- 📊 Sharpe ratio (risk-adjusted returns)
- 📉 Maximum drawdown analysis
- 🎯 Diversification metrics
- 💰 Value at Risk (VaR) calculation
- 💡 Smart rebalancing recommendations

**Usage:**
```bash
# Analyze portfolio with optimization metrics
python fetch_portfolio.py --portfolio-summary | \
python portfolio_optimizer.py --format text

# JSON output
python fetch_portfolio.py --portfolio-summary | \
python portfolio_optimizer.py

# Custom risk-free rate
python fetch_portfolio.py --portfolio-summary | \
python portfolio_optimizer.py --risk-free-rate 0.03
```

**Output Example:**
```
============================================================
PORTFOLIO OPTIMIZATION ANALYSIS
============================================================

Total Portfolio Value: $10,250.50

📊 Current Allocation:
  BTC: 50.00% ($5,125.25)
  ETH: 30.00% ($3,075.15)
  SOL: 20.00% ($2,050.10)

🔗 Correlation Matrix:
         BTC     ETH     SOL
 BTC    1.00    0.65    0.42
 ETH    0.65    1.00    0.58
 SOL    0.42    0.58    1.00

📈 Risk-Adjusted Performance:
  Sharpe Ratio: 1.450 (Good)
  Sortino Ratio: 1.820
  Max Drawdown: -35.2%
  VaR (95%): 4.25%
  VaR (99%): 6.80%

🎯 Diversification Ratio: 1.87 (Well-diversified)

💡 Rebalancing Recommendations:
  BTC (50.0%): Consider reducing allocation
    Reason: Concentration risk (>50%)
```

**Risk Metrics Explained:**

| Metric | Good Range | Interpretation |
|--------|------------|----------------|
| **Sharpe Ratio** | >1.0 | Risk-adjusted return quality |
| **Sortino Ratio** | >1.0 | Downside risk-adjusted return |
| **Max Drawdown** | <40% | Worst historical decline |
| **VaR 95%** | <5% | 95% confidence loss limit |
| **Diversification** | >1.5 | Portfolio diversification quality |

### Combined Advanced Workflow

```bash
# Complete advanced analysis pipeline
python fetch_data.py --pair BTC/USD --count 200 | \
python apply_rules.py | \
python advanced_analysis.py --format text | \
tee advanced_report.txt

# Portfolio optimization with advanced metrics
python fetch_portfolio.py --portfolio-summary | \
python portfolio_optimizer.py --format text | \
tee portfolio_optimization.txt

# Multi-asset screening (future enhancement)
# Coming soon: Screen multiple pairs for opportunities
```

## Configuration Thresholds

Default analysis thresholds (tunable):

| Metric | Default | Range | Interpretation |
|--------|---------|-------|-----------------|
| Momentum | 2.0σ | 1.0-3.0 | Price momentum strength |
| Volatility | 2.5% | 0.5-5.0% | Annualized vol ceiling |
| RSI | 30/70 | 20-80 | Overbought/oversold bounds |
| MA Fast | 12 | 5-20 | Short-term trend |
| MA Slow | 26 | 20-50 | Long-term trend |
| **ATR Period** | 14 | 7-28 | Volatility lookback |
| **Stoch RSI** | 14/3/3 | - | RSI/K/D periods |
| **S/R Threshold** | 2% | 1-5% | Level clustering |

See `.github/copilot-skills/tools/kraken-analyst/reference.md` for detailed threshold guidelines.

## Rule-Based Signal Logic

### Signal Generation

```
IF momentum > 2.0σ AND rsi < 70 AND ma_fast > ma_slow AND volatility < 3.75%
  THEN signal = "BUY"

IF momentum < -2.0σ AND rsi > 30 AND ma_fast < ma_slow AND volatility < 3.75%
  THEN signal = "SELL"

ELSE
  signal = "HOLD"
```

### Confidence Scoring

Confidence ranges 0.0-1.0 based on:
- Agreement between indicators
- Trend alignment
- Volatility adjustment
- Volume confirmation

## API Reference

### Supported Pairs

**Major Pairs (Kraken Format):**
- `BTC/USD` → `XXBTZUSD`
- `ETH/USD` → `XETHZUSD`
- `XRP/USD` → `XXRPZUSD`
- `ADA/USD` → `ADAUSD`
- `SOL/USD` → `SOLUSD`
- `DOT/USD` → `DOTUSD`
- `LINK/USD` → `LINKUSD`
- `DOGE/USD` → `XDGUSD`
- `MATIC/USD` → `MATICUSD`

See [Kraken API Docs - Asset Pairs](https://docs.kraken.com/api/docs/rest-api/get-tradable-asset-pairs) for complete list.

### Rate Limits

- Public endpoints: 15-20 requests/second
- Scripts implement 0.5s delays between requests by default
- Increase `--rate-limit` if rate limited

### Supported Intervals

| Minutes | Label | Use Case |
|---------|-------|----------|
| 1 | 1m | Scalping |
| 5 | 5m | Day trading |
| 15 | 15m | Short-term swing |
| 30 | 30m | Swing trading |
| 60 | 1h | **Standard** (recommended) |
| 240 | 4h | Position trading |
| 1440 | 1d | Long-term trend |
| 10080 | 1w | Weekly analysis |
| 21600 | 15d | Bi-weekly |

## Examples

### Example 1: Quick Bitcoin Analysis

```bash
python fetch_data.py --pair BTC/USD --interval 60 --count 50 | \
python apply_rules.py | \
python format_output.py --format markdown
```

### Example 2: Multi-Pair Comparison

```bash
for pair in BTC/USD ETH/USD XRP/USD SOL/USD; do
  echo "=== $pair ==="
  python fetch_data.py --pair $pair --interval 60 --count 24 | \
  python apply_rules.py | \
  python format_output.py --format text
  echo ""
done
```

### Example 3: Custom Analysis Parameters

```bash
python fetch_data.py --pair ETH/USD --interval 15 --count 100 | \
python apply_rules.py \
  --momentum-threshold 1.5 \
  --volatility-threshold 3.0 \
  --rsi-period 20 | \
python format_output.py --include-charts
```

### Example 4: Daily Summary

```bash
python fetch_data.py --pair BTC/USD --interval 1440 --count 30 | \
python apply_rules.py | \
python format_output.py --format markdown > btc_daily_summary.md
```

## Extend the Skill

### Adding Custom Indicators

Edit `apply_rules.py` to add new indicator calculations:

```python
def calculate_bollinger_bands(self, prices: List[float], period: int = 20, std_dev: int = 2):
    """Add Bollinger Bands analysis"""
    ma = self.calculate_moving_average(prices, period)
    # ... implementation
```

### Modifying Signal Logic

Update `_generate_signal()` in `apply_rules.py`:

```python
def _generate_signal(self, momentum, rsi, ma_trend, volatility):
    # Add custom conditions
    if momentum > 3.0 and rsi < 60:
        return "STRONG_BUY", 0.9
    # ... rest of logic
```

## Error Handling

### Common Issues

**API Connection Error:**
```
ERROR: Failed to connect to Kraken API
```
→ Check internet connection and Kraken API status

**Invalid Pair:**
```
ERROR: Kraken API error: ['EQuery:Unknown asset pair']
```
→ Use valid pairs (see API Reference above) or check with `--list-pairs`

**Rate Limited:**
```
ERROR: HTTP 429: Too Many Requests
```
→ Scripts automatically implement rate limiting; increase `--rate-limit` parameter

**Insufficient Data:**
```
ERROR: Insufficient data. Need at least 46 candles, got 20
```
→ Increase `--count` parameter or use longer interval

## Related Skills

- `/kraken` - Full Kraken API documentation reference
- `/create-skill` - Customize this skill further
- `/mcp-builder` - Build MCP server wrapper for this skill

## Resources

- **Kraken REST API**: https://docs.kraken.com/api/docs/rest-api/get-ohlc-data
- **Skill Prompt**: `.github/prompts/kraken-analyst.skill.prompt.md`
- **Instructions**: `.github/instructions/kraken-analyst.instructions.md`
- **Scripts**: `.github/copilot-skills/tools/kraken-analyst/scripts/`
- **Technical Reference**: `.github/copilot-skills/tools/kraken-analyst/reference.md`

## Environment Configuration

### Public Endpoints (No Setup Required)

This skill uses **public Kraken API endpoints** that do NOT require authentication:
- ✅ `/public/OHLC` - OHLC/candlestick data
- ✅ `/public/Ticker` - Ticker information
- ✅ `/public/AssetPairs` - Trading pairs

**No API key needed** - scripts work immediately out of the box!

### Configuration File (Optional)

A `.env` file is provided for optional configuration:

```bash
# Copy the example file
cp .github/copilot-skills/tools/kraken-analyst/.env.example \
   .github/copilot-skills/tools/kraken-analyst/.env
```

**Available Configuration:**
```bash
# API Configuration
KRAKEN_API_URL=https://api.kraken.com
RATE_LIMIT=0.5

# Default Analysis Parameters
MOMENTUM_THRESHOLD=2.0
VOLATILITY_THRESHOLD=2.5
RSI_PERIOD=14
MA_FAST=12
MA_SLOW=26
DEFAULT_INTERVAL=60
DEFAULT_COUNT=100
```

> **Note**: The current scripts use command-line arguments and do not read from `.env`. The file is provided as a template if you want to extend the skill with environment-based configuration.

### Private Endpoints (Future Extension)

If you want to extend this skill to use **private Kraken API endpoints** (account balances, trading, order management), you'll need to:

1. **Create API Keys** at [Kraken Settings → API](https://www.kraken.com/u/security/api)
2. **Add to `.env` file**:
   ```bash
   KRAKEN_API_KEY=your_api_key_here
   KRAKEN_PRIVATE_KEY=your_private_key_here
   ```
3. **Implement authentication** in scripts (see [Kraken API Auth Docs](https://docs.kraken.com/api/docs/guides/spot-rest-auth))

**Security Note**: The `.env` file is already in `.gitignore` to prevent accidental commits of sensitive credentials.

## Dependencies

**Python 3.7+** - Standard library only, no external packages required:
- `json` - Data serialization
- `urllib` - HTTP requests
- `argparse` - CLI parsing
- `datetime` - Timestamp handling

**No API keys or authentication required** for public endpoint usage.

## License

MIT License

---

**Version**: 1.0.0  
**Last Updated**: October 2025  
**Maintained By**: Copilot Skills Architecture  
**Built From**: Official Kraken API Documentation
