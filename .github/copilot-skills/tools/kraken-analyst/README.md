---
name: kraken-analyst
description: Fetches live Kraken crypto data and applies quantitative rule-sets for strategy insights.
version: "1.0.0"
tags: ["crypto", "market", "kraken", "strategy", "analysis"]
dependencies: ["python3"]
license: MIT
---

# Kraken Analyst Copilot Skill

A quantitative analysis skill for fetching live cryptocurrency market data from Kraken and applying rule-based strategy signals. Built using official Kraken API documentation.

## Overview

The Kraken Analyst skill provides:

- **Live Data Fetching** - Real-time OHLC data from Kraken REST API v0
- **Quantitative Analysis** - Momentum, volatility, and trend calculations
- **Rule-Based Signals** - BUY, SELL, HOLD recommendations based on configurable thresholds
- **Structured Output** - JSON + Markdown formatted reports
- **Portfolio Management** - Account balance tracking, allocation analysis, and rebalancing recommendations (requires API keys)

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

To use portfolio management features, you need Kraken API credentials:

1. **Login to Kraken**: https://www.kraken.com
2. **Go to Settings → API**
3. **Create New API Key** with permissions:
   - ✅ Query Funds (required for balances)
   - ✅ Query Open Orders & Trades (required for order history)
   - ✅ Query Closed Orders & Trades (optional)
4. **Copy API Key and Private Key**
5. **Configure Environment**:
   ```bash
   cp .github/copilot-skills/tools/kraken-analyst/.env.example \
      .github/copilot-skills/tools/kraken-analyst/.env
   
   # Edit .env and add your credentials:
   # KRAKEN_API_KEY=your-api-key-here
   # KRAKEN_PRIVATE_KEY=your-private-key-here
   ```

**Security Best Practices:**
- ✅ Never commit `.env` file to git
- ✅ Use API key restrictions (IP whitelist, expiration dates)
- ✅ Grant minimum required permissions
- ✅ Rotate keys regularly
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

Fetches account portfolio data from private API endpoints.

**Requires**: API credentials in `.env` file

**Usage:**
```bash
# Get account balances
python fetch_portfolio.py --balances

# Get complete portfolio summary with USD values
python fetch_portfolio.py --portfolio-summary

# Get open orders
python fetch_portfolio.py --open-orders

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
  "timestamp": 1697834523.456,
  "total_value_usd": 377.69,
  "asset_count": 4,
  "portfolio": [
    {
      "asset": "XXBT",
      "amount": 0.00241234,
      "price_usd": 108725.90,
      "value_usd": 262.39,
      "weight": 69.46
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

## Configuration Thresholds

Default analysis thresholds (tunable):

| Metric | Default | Range | Interpretation |
|--------|---------|-------|-----------------|
| Momentum | 2.0σ | 1.0-3.0 | Price momentum strength |
| Volatility | 2.5% | 0.5-5.0% | Annualized vol ceiling |
| RSI | 30/70 | 20-80 | Overbought/oversold bounds |
| MA Fast | 12 | 5-20 | Short-term trend |
| MA Slow | 26 | 20-50 | Long-term trend |

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
