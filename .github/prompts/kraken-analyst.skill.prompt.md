---
description: Fetches live Kraken crypto data and applies quantitative rule-sets for strategy insights. Includes portfolio management.
---

# Kraken Analyst

**Purpose**: Analyze cryptocurrency market data from Kraken exchange using quantitative rule-based strategies and manage portfolio allocation.

## When to Use This Skill

Use this skill when:
- Analyzing cryptocurrency market trends (BTC, ETH, XRP, etc.)
- Generating BUY/SELL/HOLD signals from technical indicators
- Fetching live OHLC data from Kraken exchange
- Calculating momentum, volatility, RSI, and moving averages
- Creating formatted market analysis reports
- Tracking portfolio balances and allocation (requires API keys)
- Getting rebalancing recommendations

**Keywords**: crypto, cryptocurrency, kraken, market data, trading, signals, strategy, bitcoin, ethereum, technical analysis, momentum, RSI, moving average, portfolio, balances, allocation

## User Intent Decision Tree

**Before starting any analysis**, determine what the user wants:

### 1️⃣ Quick Question (Informational)
**User asks**: "What's BTC's current price?" or "Is ETH oversold?"
**Action**: Use `fetch_data.py` → `apply_rules.py` → provide quick answer
**No**: Full pipeline, portfolio analysis, or reports

### 2️⃣ Market Analysis (Public API - No Keys Needed)
**User asks**: "Analyze BTC" or "Should I buy ETH?" or "SOL technical analysis"
**Action**: Run full market analysis pipeline with technical indicators
**Scripts**: `fetch_data.py` → `apply_rules.py` → `advanced_analysis.py` → `format_output.py`
**Requirements**: None (public API)

### 3️⃣ Portfolio Review (Private API - Requires Keys)
**User asks**: "Review my portfolio" or "What do I own?" or "Portfolio analysis"
**Action**: 
  1. Check if `.env` configured (auto-loaded by `kraken_auth.py`)
  2. Fetch portfolio with `fetch_portfolio.py --portfolio-summary`
  3. Get market analysis for each holding
  4. Provide comprehensive breakdown with recommendations
**Requirements**: KRAKEN_API_KEY and KRAKEN_PRIVATE_KEY in `.env`

### 4️⃣ Partial Portfolio Query (Private API)
**User asks**: "How much BTC do I have?" or "My SOL balance"
**Action**: Use `fetch_portfolio.py --balances` for quick answer
**Requirements**: API keys in `.env`

### 5️⃣ Trading History (Private API)
**User asks**: "My recent trades" or "Trading history"
**Action**: Use `fetch_portfolio.py --trade-history --count N`
**Requirements**: API keys + "Query Closed Orders & Trades" permission

## Quick Reference

### Common Workflow

1. **Fetch market data** from Kraken API
2. **Apply analysis rules** (momentum, volatility, RSI, MA)
3. **Generate signal** (BUY/SELL/HOLD with confidence)
4. **Format output** (markdown report or JSON)

### Code Examples

**Example 1: Basic Analysis**
```bash
python .github/copilot-skills/kraken-analyst/scripts/fetch_data.py --pair BTC/USD --interval 60 --count 100 | \
python .github/copilot-skills/kraken-analyst/scripts/apply_rules.py | \
python .github/copilot-skills/kraken-analyst/scripts/format_output.py
```

**Example 2: Custom Thresholds**
```bash
python .github/copilot-skills/kraken-analyst/scripts/fetch_data.py --pair ETH/USD --interval 60 | \
python .github/copilot-skills/kraken-analyst/scripts/apply_rules.py \
  --momentum-threshold 1.5 \
  --volatility-threshold 3.0 \
  --rsi-period 20 | \
python .github/copilot-skills/kraken-analyst/scripts/format_output.py --include-charts
```

**Example 3: Multi-Pair Analysis**
```bash
for pair in BTC/USD ETH/USD SOL/USD; do
  python .github/copilot-skills/kraken-analyst/scripts/fetch_data.py --pair $pair | \
  python .github/copilot-skills/kraken-analyst/scripts/apply_rules.py | \
  python .github/copilot-skills/kraken-analyst/scripts/format_output.py --format text
done
```

**Example 4: Portfolio Analysis (Requires API Keys)**
```bash
# Complete portfolio review with market analysis
python .github/copilot-skills/kraken-analyst/scripts/fetch_portfolio.py --portfolio-summary

# The script auto-loads .env file - no manual env loading needed!
```

**Example 5: Quick Balance Check**
```bash
# Just see what you own
python .github/copilot-skills/kraken-analyst/scripts/fetch_portfolio.py --balances
```

## Supported Pairs

**Major cryptocurrencies:**
- BTC/USD, BTC/EUR, BTC/GBP
- ETH/USD, ETH/EUR, ETH/BTC
- XRP/USD, XRP/EUR
- ADA/USD, SOL/USD, DOT/USD
- LINK/USD, DOGE/USD, MATIC/USD

Use `--list-pairs` to see all supported pairs.

## Analysis Indicators

### Momentum
- Measures price deviation from 50-period MA in standard deviations
- Threshold: ±2.0σ (configurable)
- Interpretation: >2.0σ = strong upward, <-2.0σ = strong downward

### Volatility
- Annualized volatility calculated from 20-period returns
- Threshold: 2.5% (configurable)
- Filters extreme market conditions

### RSI (Relative Strength Index)
- 14-period RSI (configurable)
- Overbought: >70
- Oversold: <30
- Neutral: 30-70

### Moving Averages
- Fast MA: 12 periods (default)
- Slow MA: 26 periods (default)
- Trend: bullish when MA_fast > MA_slow

## Signal Generation Logic

```
BUY Signal:
  momentum > 2.0σ AND
  rsi < 70 AND
  ma_fast > ma_slow AND
  volatility < 3.75%

SELL Signal:
  momentum < -2.0σ AND
  rsi > 30 AND
  ma_fast < ma_slow AND
  volatility < 3.75%

HOLD Signal:
  No clear directional signal
```

## Confidence Scoring

Confidence (0.0-1.0) adjusted by:
- **Volatility**: Higher vol = lower confidence
- **RSI extremes**: >75 or <25 reduces confidence
- **Volume**: Higher volume = higher confidence
- **Indicator agreement**: More aligned = higher confidence

## Scripts Reference

### fetch_data.py
Fetches OHLC data from Kraken REST API v0.

**Key Parameters:**
- `--pair` - Trading pair (BTC/USD, XXBTZUSD)
- `--interval` - Minutes: 1, 5, 15, 30, 60, 240, 1440, 10080, 21600
- `--count` - Number of candles (1-720)
- `--rate-limit` - Delay between requests (default: 0.5s)

**Output:** JSON with OHLC data + metadata

### apply_rules.py
Applies quantitative analysis rules.

**Key Parameters:**
- `--momentum-threshold` - Std devs for momentum (default: 2.0)
- `--volatility-threshold` - Annual vol % (default: 2.5)
- `--rsi-period` - RSI lookback (default: 14)
- `--ma-fast` / `--ma-slow` - MA periods (default: 12/26)

**Output:** JSON with analysis + signal + confidence

### format_output.py
Generates human-readable reports.

**Key Parameters:**
- `--format` - markdown, text, or json (default: markdown)
- `--include-charts` - Add ASCII charts (default: false)

**Output:** Formatted report with signal explanation

## Workflows

### Workflow 1: Quick Market Check

**Goal:** Get current signal for BTC/USD

```bash
cd .github/copilot-skills/kraken-analyst/scripts
python fetch_data.py --pair BTC/USD --interval 60 --count 50 | \
python apply_rules.py | \
python format_output.py --format text
```

### Workflow 2: Daily Summary Report

**Goal:** Generate daily analysis with charts

```bash
cd .github/copilot-skills/kraken-analyst/scripts
python fetch_data.py --pair ETH/USD --interval 1440 --count 30 | \
python apply_rules.py | \
python format_output.py --format markdown --include-charts > daily_report.md
```

### Workflow 3: Multi-Timeframe Analysis

**Goal:** Compare signals across timeframes

```bash
cd .github/copilot-skills/kraken-analyst/scripts
for interval in 60 240 1440; do
  echo "=== Interval: $interval minutes ==="
  python fetch_data.py --pair BTC/USD --interval $interval --count 100 | \
  python apply_rules.py | \
  python format_output.py --format text
done
```

### Workflow 4: Custom Strategy

**Goal:** Use aggressive thresholds for scalping

```bash
cd .github/copilot-skills/kraken-analyst/scripts
python fetch_data.py --pair SOL/USD --interval 5 --count 200 | \
python apply_rules.py \
  --momentum-threshold 1.0 \
  --volatility-threshold 5.0 \
  --rsi-period 7 | \
python format_output.py
```

### Workflow 5: Complete Portfolio Review

**Goal:** Comprehensive portfolio analysis with market insights

**Prerequisites**: 
1. Create `.env` file in `kraken-analyst/` directory
2. Add your API credentials:
   ```
   KRAKEN_API_KEY=your-api-key-here
   KRAKEN_PRIVATE_KEY=your-private-key-base64-here
   ```
3. Scripts automatically load `.env` - no manual sourcing needed!

**Steps:**
```bash
cd .github/copilot-skills/kraken-analyst/scripts

# 1. Get portfolio summary (includes spot + Kraken Earn)
python3 fetch_portfolio.py --portfolio-summary --format pretty

# 2. For each major holding, get technical analysis
# BTC analysis
python3 fetch_data.py --pair BTC/USD --interval 1440 --count 90 | \
  python3 apply_rules.py | python3 format_output.py --format text

# ETH analysis  
python3 fetch_data.py --pair ETH/USD --interval 1440 --count 90 | \
  python3 apply_rules.py | python3 format_output.py --format text

# 3. Get advanced indicators
python3 fetch_data.py --pair BTC/USD --interval 1440 --count 90 | \
  python3 advanced_analysis.py --format text
```

**Output includes**:
- Total portfolio value (spot + Kraken Earn staking)
- Asset allocation percentages
- Current USD values per holding
- Market analysis for each asset
- Support/Resistance levels
- Technical indicators (RSI, Momentum, Ichimoku, etc.)
- BUY/SELL/HOLD signals with confidence scores

### Workflow 6: Quick Balance Check

**Goal:** See what you own without full analysis

```bash
cd .github/copilot-skills/kraken-analyst/scripts
python3 fetch_portfolio.py --balances
```

### Workflow 7: Trading History Analysis

**Goal:** Review recent trading activity

```bash
cd .github/copilot-skills/kraken-analyst/scripts
python3 fetch_portfolio.py --trade-history --count 30
```

## Reference Documentation

Comprehensive docs in `.github/copilot-skills/kraken-analyst/`:

- **README.md** - Complete skill guide with examples
- **reference.md** - Deep technical reference (formulas, backtesting)
- **scripts/** - fetch_data.py, apply_rules.py, format_output.py

For Kraken API details, see:
- **`.github/copilot-skills/kraken/references/rest_api.md`** - Full API documentation (4600+ lines)

## How to Use

### For Quick Answers
Ask directly about crypto analysis or Kraken market data.

### For Implementation
1. Use the scripts in `scripts/` directory
2. Pipe output between scripts for full pipeline
3. Customize thresholds via command-line args

### For Detailed Information
- Check `README.md` for complete usage guide
- Check `reference.md` for technical formulas
- Check `/kraken` skill for full API documentation

## Tips

✅ **Do:**
- Start with default thresholds (momentum=2.0, volatility=2.5)
- Use 60-minute interval for balanced analysis
- Fetch 100+ candles for reliable indicators
- Compare signals across multiple timeframes

⚠️ **Don't:**
- Trade solely based on signals (use as reference)
- Ignore confidence scores
- Use extreme thresholds without backtesting
- Analyze with insufficient data (<50 candles)

## Related Skills

- `/kraken` - Full Kraken API documentation
- `/create-skill` - Customize this skill
- `/mcp-builder` - Build MCP server wrapper

## More Information

- **Skill Directory**: `.github/copilot-skills/kraken-analyst/`
- **Kraken API Docs**: https://docs.kraken.com/api/
- **Generated From**: Official Kraken API documentation (200 pages scraped)
