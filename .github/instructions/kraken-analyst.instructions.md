# Kraken Analyst Instructions

Auto-loaded when: `/*.py, /*.js, /*.ts, /crypto*, /trading*, /market*, /kraken*, /portfolio*`

## Core Capabilities

### Public API Features (No Authentication Required)
- Market data fetching (OHLC candles)
- Technical analysis (momentum, RSI, MA, volatility)
- Signal generation (BUY/SELL/HOLD)
- Multi-timeframe analysis
- Real-time price tracking

### Private API Features (Requires API Keys)
- Portfolio balance tracking
- Account allocation analysis
- Rebalancing recommendations
- Trade history and volume
- Open orders management
- Fee analysis

## Default Behaviors

### For Public Endpoints
1. Use official Kraken API endpoints from https://api.kraken.com/0/public
2. Respect rate limits (0.5s minimum between requests)
3. Validate input parameters before API calls
4. Provide deterministic JSON output to stdout
5. Log errors to stderr without halting pipeline

### For Private Endpoints
1. Credentials auto-load - `kraken_auth.py` automatically loads `.env` from parent directory on import
2. No manual sourcing needed - Just run scripts directly (e.g., `python3 fetch_portfolio.py --balances`)
3. Check authentication before making private API calls
4. Generate proper signatures for authenticated requests
5. Handle nonce correctly (use millisecond timestamp)
6. Respect rate limits (0.5-1.0s between requests for private endpoints)
7. Never log or expose API credentials

Important: The `.env` file is now automatically loaded when `kraken_auth.py` is imported. Users do NOT need to manually source the file or export variables before running portfolio scripts.

## Common Workflows

### Market Analysis (Public API)

#### Fetch Market Data
```bash
python fetch_data.py --pair BTC/USD --interval 60 --count 100
```

#### Apply Analysis
```bash
python fetch_data.py --pair BTC/USD | python apply_rules.py
```

#### Generate Report
```bash
python fetch_data.py --pair BTC/USD | python apply_rules.py | python format_output.py
```

### Portfolio Management (Private API)

Prerequisites: 
- Create `.env` file in `kraken-analyst/` directory (parent of `scripts/`)
- Add: `KRAKEN_API_KEY=...` and `KRAKEN_PRIVATE_KEY=...`
- Scripts auto-load `.env` on import - no manual env setup needed!

#### Get Account Balances
```bash
# Just run directly - .env is auto-loaded
python3 fetch_portfolio.py --balances
```

Output: JSON with all non-zero balances (spot + futures/spreads)

#### Get Portfolio Summary
```bash
# Includes spot holdings + Kraken Earn (staking) allocations
python3 fetch_portfolio.py --portfolio-summary --format pretty
```

Output Structure:
```json
{
  "total_value_usd": 373.87,
  "spot_value_usd": 0.02,
  "earn_value_usd": 373.85,
  "spot_portfolio": [ /* spot holdings */ ],
  "earn_allocations": [ /* staked assets with APR */ ],
  "futures_dust": [ /* negligible futures contracts */ ]
}
```

Key Features:
- ✅ Automatically fetches Kraken Earn (staking) allocations
- ✅ Combines spot + earn for total portfolio value
- ✅ Maps futures/spread contracts to spot prices
- ✅ Calculates allocation percentages
- ✅ Provides current USD values using live ticker prices

#### Get Trade History
```bash
python3 fetch_portfolio.py --trade-history --count 30
```

#### Get Open Orders
```bash
python3 fetch_portfolio.py --open-orders
```

#### Complete Portfolio Analysis
```bash
# Get portfolio data
python3 fetch_portfolio.py --portfolio-summary > portfolio.json

# Then analyze each major holding with market data
python3 fetch_data.py --pair BTC/USD --interval 1440 --count 90 | \
  python3 apply_rules.py | python3 advanced_analysis.py
```

## Security Best Practices

### API Credentials Management

✅ Do:
- Store credentials in `.env` file (never commit to git)
- Place `.env` in `kraken-analyst/` directory (parent of `scripts/`)
- Use environment variables for sensitive data  
- Set `.gitignore` to exclude `.env` files
- Use API key restrictions (IP whitelist, expiration)
- Grant minimum required permissions
- Rotate keys regularly

❌ Don't:
- Hardcode API keys in source code
- Commit `.env` with real credentials
- Share API keys in chat or logs
- Use production keys for testing
- Grant unnecessary permissions
- Manually export env vars (scripts auto-load `.env`)

### .env File Auto-Loading

How it works: `kraken_auth.py` automatically loads `.env` when imported

File location: `kraken-analyst/.env` (parent directory of `scripts/`)

What this means:
- ✅ Run scripts directly: `python3 fetch_portfolio.py --balances`
- ✅ No `source .env` or `export` commands needed
- ❌ Don't manually load environment variables

### Authentication Code Patterns

Correct - Load from environment:
```python
api_key = os.getenv("KRAKEN_API_KEY", "")
private_key = os.getenv("KRAKEN_PRIVATE_KEY", "")

if not api_key or not private_key:
    print("ERROR: API credentials not configured", file=sys.stderr)
    sys.exit(1)
```

Avoid - Hardcoded credentials:
```python
api_key = "YOUR_API_KEY_HERE"  # NEVER DO THIS
private_key = "YOUR_PRIVATE_KEY"  # NEVER DO THIS
```

### Error Handling for Private Endpoints

Correct:
```python
result = auth.query_private("Balance")
if result is None:
    print("ERROR: Authentication failed", file=sys.stderr)
    sys.exit(1)
```

## Quality Guidelines

### ✅ Use Official API Format

Correct - Kraken native format:
```python
api_pair = "XXBTZUSD"
url = f"{BASE_URL}/OHLC?pair={api_pair}&interval=60"
```

Avoid - Invalid format:
```python
api_pair = "BTC-USD"  # Wrong separator
api_pair = "btc/usd"  # Wrong case
```

### ✅ Handle API Errors Gracefully

Correct:
```python
if data.get('error') and len(data['error']) > 0:
    print(f"ERROR: Kraken API error: {data['error']}", file=sys.stderr)
    return None
```

Avoid:
```python
# Don't crash on API errors
result = data['result']  # May not exist if error
```

### ✅ Follow Pipeline Architecture

Correct - Modular scripts:
```bash
# Each script does one thing well
fetch_data.py → apply_rules.py → format_output.py
```

Avoid - Monolithic scripts:
```python
# Don't combine fetching + analysis in one script
```

### ✅ Use Standard Library Only

Correct:
```python
import urllib.request
import urllib.parse
import json
```

Avoid:
```python
import requests  # External dependency
import pandas  # External dependency
```

## Default Analysis Thresholds

| Parameter | Default | Range | Purpose |
|-----------|---------|-------|---------|
| `momentum_threshold` | 2.0σ | 1.0-3.0 | Price momentum strength |
| `volatility_threshold` | 2.5% | 0.5-5.0% | Annualized volatility ceiling |
| `rsi_period` | 14 | 7-21 | RSI lookback window |
| `ma_fast` | 12 | 5-20 | Short-term trend MA |
| `ma_slow` | 26 | 20-50 | Long-term trend MA |

## Configuration Best Practices

### Momentum Threshold

Standard (2.0σ) - Balanced sensitivity
```bash
python apply_rules.py --momentum-threshold 2.0
```

Conservative (2.5σ) - Fewer but stronger signals
```bash
python apply_rules.py --momentum-threshold 2.5
```

Aggressive (1.5σ) - More frequent signals
```bash
python apply_rules.py --momentum-threshold 1.5
```

### Volatility Threshold

Normal Markets (2.5%) - Filter extreme volatility
```bash
python apply_rules.py --volatility-threshold 2.5
```

Crypto Bull Run (4.0%) - Allow higher volatility
```bash
python apply_rules.py --volatility-threshold 4.0
```

Low Vol Markets (1.5%) - Strict filtering
```bash
python apply_rules.py --volatility-threshold 1.5
```

## Error Handling Patterns

### Pattern 1: API Connection Error

```python
try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode())
except urllib.error.URLError as e:
    print(f"ERROR: Failed to connect: {e.reason}", file=sys.stderr)
    return None
```

### Pattern 2: Invalid Input

```python
if not (1 <= count <= 720):
    print(f"ERROR: Count must be 1-720, got {count}", file=sys.stderr)
    return None
```

### Pattern 3: Rate Limiting

```python
def _rate_limit_wait(self):
    elapsed = time.time() - self.last_request_time
    if elapsed < self.rate_limit:
        time.sleep(self.rate_limit - elapsed)
    self.last_request_time = time.time()
```

## Supported Trading Pairs

Major Crypto Pairs (Kraken Format):

| User Format | Kraken API Format |
|-------------|-------------------|
| BTC/USD | XXBTZUSD |
| ETH/USD | XETHZUSD |
| XRP/USD | XXRPZUSD |
| ADA/USD | ADAUSD |
| SOL/USD | SOLUSD |
| DOT/USD | DOTUSD |
| LINK/USD | LINKUSD |
| DOGE/USD | XDGUSD |
| MATIC/USD | MATICUSD |

Format Rules:
- Major crypto (BTC, ETH, LTC, XRP): Add 'X' prefix
- Fiat (USD, EUR, GBP): Add 'Z' prefix
- New assets (ADA, SOL, DOT): Use as-is

## Interval Guidelines

| Interval | Minutes | Use Case | Recommended Count |
|----------|---------|----------|-------------------|
| 1m | 1 | Scalping | 200+ |
| 5m | 5 | Day trading | 100-200 |
| 15m | 15 | Short swing | 100 |
| 30m | 30 | Swing trading | 50-100 |
| 1h | 60 | Standard | 100 |
| 4h | 240 | Position | 50 |
| 1d | 1440 | Long-term | 30-50 |
| 1w | 10080 | Weekly | 20-30 |

Recommendation: Use 60-minute (1h) interval with 100 candles for balanced analysis.

## Signal Interpretation

### BUY Signal (Confidence: 0.7-1.0)

Conditions Met:
- Momentum > threshold (strong upward movement)
- RSI < 70 (not overbought)
- MA Fast > MA Slow (bullish trend)
- Volatility < threshold * 1.5 (stable)

Action: Consider long position or holding

### SELL Signal (Confidence: 0.7-1.0)

Conditions Met:
- Momentum < -threshold (strong downward movement)
- RSI > 30 (not oversold)
- MA Fast < MA Slow (bearish trend)
- Volatility < threshold * 1.5 (stable)

Action: Consider short position or exit

### HOLD Signal (Confidence: 0.3-0.7)

Conditions:
- Momentum within ±threshold (neutral)
- Mixed indicator signals
- High volatility (>threshold * 1.5)

Action: Wait for clearer signal

## Confidence Score Factors

Base Confidence:
- Strong signal conditions: 0.8
- Moderate signal: 0.5

Adjustments:
- High volatility: × 0.5-1.0 (reduces confidence)
- RSI extremes (>75, <25): × 0.8 (uncertain)
- Volume confirmation (1.5x avg): × 1.1 (increases confidence)
- Low volume (0.5x avg): × 0.8 (reduces confidence)

Final Range: 0.0-1.0 (clamped)

## Testing Scripts

### Test 1: Fetch Data

```bash
# Should output JSON with 50 candles
python fetch_data.py --pair BTC/USD --interval 60 --count 50
```

Expected: JSON with `data_points: 50` and array of OHLC candles

### Test 2: Apply Rules

```bash
# Should output analysis with signal
echo '{"pair":"BTC/USD","interval":60,"data":[...]}' | python apply_rules.py
```

Expected: JSON with `signal`, `confidence`, and `analysis` fields

### Test 3: Format Output

```bash
# Should output markdown report
echo '{"pair":"BTC/USD","signal":"BUY","confidence":0.82,...}' | \
python format_output.py --format markdown
```

Expected: Markdown formatted report with tables and signal explanation

### Test 4: Full Pipeline

```bash
# Should complete end-to-end
python fetch_data.py --pair ETH/USD --interval 60 --count 100 | \
python apply_rules.py | \
python format_output.py > report.md
```

Expected: Markdown file with complete analysis report

## Performance Guidelines

API Response Times:
- Public OHLC endpoint: 200-500ms typical
- Network latency: 50-200ms additional

Processing Times:
- fetch_data.py: <2s for 100 candles
- apply_rules.py: <100ms
- format_output.py: <50ms

Memory Usage:
- ~5MB for 720 candles (max dataset)

## Security Considerations

✅ Safe:
- Public API endpoints (no auth required)
- Read-only data fetching
- No sensitive data stored

⚠️ Note:
- Scripts do NOT handle private API calls (trading, balances)
- No API keys or credentials needed
- No trading execution (analysis only)

## Troubleshooting

### Issue: "Invalid pair error"

```bash
ERROR: Kraken API error: ['EQuery:Unknown asset pair']
```

Solution: Use valid format or check with `--list-pairs`

### Issue: "Rate limited (429)"

```bash
ERROR: HTTP 429: Too Many Requests
```

Solution: Increase `--rate-limit` parameter:
```bash
python fetch_data.py --rate-limit 1.0 --pair BTC/USD
```

### Issue: "Insufficient data for analysis"

```bash
ERROR: Insufficient data. Need at least 46 candles, got 20
```

Solution: Increase `--count` parameter:
```bash
python fetch_data.py --pair BTC/USD --count 100
```

### Issue: "Connection timeout"

```bash
ERROR: Failed to connect: timed out
```

Solution: Check internet connection and Kraken API status

## Related Files

- Skill Prompt: `.github/prompts/kraken-analyst.skill.prompt.md`
- Skill Directory: `.github/copilot-skills/kraken-analyst/`
- Scripts: `fetch_data.py`, `apply_rules.py`, `format_output.py`
- API Docs: `.github/copilot-skills/kraken/references/rest_api.md`

## Dependencies

Python 3.7+ (Standard library only):
- json, sys, argparse, time
- urllib.request, urllib.parse, urllib.error
- datetime, typing, dataclasses

No external packages required - Scripts are fully self-contained.