# Selected Public Findings

The exact strategy rules remain private. The following findings are included to demonstrate the research process.

## Large-sample XAUUSD research

A long historical XAUUSD dataset contained more than 100,000 completed trades.

The strategy showed positive historical expectancy over the full dataset, but:
- performance varied substantially by year,
- cost-adjusted profit factor was much weaker than the raw backtest,
- and some years approached or crossed break-even.

This showed that a single full-period metric could hide major regime variation.

## Win-rate instability

Shorter recent tests produced noticeably stronger win rates than longer historical tests.

For an asymmetric reward:risk strategy, a difference of only a few percentage points in win rate can materially change expected value.

This made regime dependence a central research question.

## Sequence research

Trade results were encoded as binary sequences.

Patterns were scanned for conditional next-trade behavior.

Some patterns showed higher historical win rates, but I treated them as hypotheses rather than conclusions because scanning many patterns creates a multiple-testing problem.

## Seasonal and time-of-day research

Performance was grouped by:
- season,
- month,
- weekday,
- hour,
- and year.

Some time windows showed stronger results than the full strategy.

These were then checked using chronological splits to distinguish persistent behavior from recent-regime effects.

## Automation and risk

The strategy was implemented as an MT5 Expert Advisor.

Different risk-per-trade levels produced very different equity curves.

This demonstrated that:
- statistical edge,
- risk sizing,
- and drawdown tolerance
must be evaluated separately.
