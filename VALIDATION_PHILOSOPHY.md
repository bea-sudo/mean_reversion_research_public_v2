# Validation Philosophy

A backtest is not evidence simply because it is profitable.

The research process used several principles.

## 1. Large samples over attractive charts

A small sample can produce almost any win rate.

Whenever possible, I expanded the historical dataset before trusting the result.

## 2. Chronological validation

Random train/test splits can be misleading in financial time series.

I therefore used chronological comparisons such as:
- older history vs newer history,
- year-by-year performance,
- rolling or block-based checks.

## 3. Cost-aware performance

A small edge can disappear after spread and slippage.

For this reason, I recalculated:
- profit factor,
- expected payoff,
- total profit,
- and break-even cost levels.

## 4. One change at a time

When testing a filter, I tried to keep the baseline strategy frozen.

Changing many parameters simultaneously makes it difficult to know what caused an improvement.

## 5. Reject weak evidence

A result was treated cautiously when:
- occurrence count was small,
- improvement existed only in one period,
- recent performance was much stronger than old performance,
- or profit factor remained close to 1.

## 6. Separate strategy quality from risk

A high-risk position size can make a weak strategy look exciting.

Risk changes the equity curve, not the underlying statistical edge.

This distinction became especially important during MT5 automation tests.
