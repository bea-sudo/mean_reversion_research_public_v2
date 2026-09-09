# Independent Quantitative Trading Research

## A student-built research project on market behavior, robustness, and automated testing

This project began with a simple question:

> **Can a trading idea that looks profitable in one period survive when it is tested across years, different market regimes, transaction costs, and thousands of trades?**

I did not want to stop at a chart that looked good.

I wanted to build a complete research process around the strategy:
- collect historical trade data,
- test it over long periods,
- measure how the edge changes,
- search for regime dependence,
- analyze trade sequences,
- study seasonal and time-of-day behavior,
- account for trading costs,
- automate execution,
- and most importantly, reject ideas when the evidence became weak.

The exact strategy rules are intentionally private. This repository focuses on the **research process, statistical thinking, engineering, and lessons learned**.

---

# Why I Built This

I became interested in quantitative finance because markets sit at the intersection of mathematics, probability, programming, psychology, and decision-making under uncertainty.

At first, it is easy to look at a profitable backtest and think:

> “I found an edge.”

The deeper I went, the more I realized that this is not enough.

A strategy can look strong because:
- one year happened to fit it,
- one market regime was unusually favorable,
- transaction costs were ignored,
- parameters were overfit,
- a pattern appeared by chance,
- or the sample was simply too small.

So the project changed.

It stopped being a project about **finding a profitable strategy** and became a project about:

> **learning how to prove myself wrong.**

That became the most important part of the research.

---

# Research Journey

The project evolved through several stages.

## 1. Baseline Strategy Research

I started with a simple rule-based mean-reversion framework.

The first goal was not optimization. It was to create a fixed baseline that could be measured repeatedly.

I tested:
- win rate,
- profit factor,
- expected value,
- drawdown,
- losing streaks,
- long vs short performance,
- and performance across different historical periods.

## 2. Long-Horizon Testing

I expanded the backtests from short recent samples to multi-year and multi-decade datasets.

One XAUUSD research set contained more than **100,000 completed trades** across roughly two decades of historical data.

This immediately exposed something that a short backtest could hide:

> performance was not constant through time.

Some years were strong. Others were weak. One period could show a healthy win rate while the long-run average sat much closer to break-even.

That pushed me toward regime analysis.

## 3. Transaction Cost Testing

I rebuilt performance metrics after applying simulated trading costs to every completed trade.

This was important because a small statistical edge can disappear once realistic friction is included.

I learned to compare:
- raw expectancy,
- cost-adjusted expectancy,
- profit factor before and after costs,
- and the maximum average cost the strategy could tolerate before its historical edge disappeared.

## 4. Trade-Sequence Research

I encoded completed trades as:

- `1` = winner
- `0` = loser

Then I built tools that scanned historical sequences such as:

`01111`, `10011`, `11111`

and measured what happened next.

The goal was not to assume that a losing streak “must” be followed by a win.

Instead, I tested conditional probabilities directly from data.

This became a practical lesson in the gambler’s fallacy, sample size, and multiple testing.

## 5. Stability Testing

I created research tools to avoid trusting a pattern only because it looked strong in the full sample.

Patterns were checked across chronological blocks.

I used ideas such as:
- minimum sample sizes,
- recent-vs-historical comparisons,
- z-score stability checks,
- and out-of-sample style chronological splits.

## 6. Risk and Automation

I converted the strategy into an MT5 Expert Advisor.

The bot:
- evaluates signals on closed candles,
- calculates dynamic position size,
- applies fixed stop-loss and take-profit rules,
- prevents duplicate positions,
- and allows the same strategy logic to be tested under different risk percentages.

This part of the project taught me that:

> a profitable strategy and a survivable strategy are not the same thing.

A high risk-per-trade setting could produce impressive growth while also producing unacceptable drawdowns.

## 7. Regime and Seasonal Analysis

When recent performance differed from long-term performance, I did not immediately optimize the strategy.

I tested whether market conditions were changing.

I analyzed:
- year,
- season,
- month,
- weekday,
- hour of day,
- long vs short direction,
- and trend-regime filters.

Some apparent effects survived chronological splits. Others disappeared once older data was separated from recent data.

That distinction became one of the central themes of the project.

---

# What This Project Is Really About

This repository is not meant to prove that I discovered a secret trading system.

It demonstrates how I think.

The project required me to combine:

- probability,
- statistics,
- programming,
- data cleaning,
- backtesting,
- risk management,
- software engineering,
- experiment design,
- and skepticism toward my own results.

The most useful moments were often the ones where the data rejected my idea.

That changed the way I approach technical problems.

Instead of asking:

> “How do I make this result look better?”

I started asking:

> “What evidence would convince me that this result is false?”

That is the mindset I want to keep developing in mathematics, quantitative research, and scientific work.

---

# Public Research Architecture

```text
Private strategy logic
        |
        v
Historical backtest
        |
        v
Completed trade export
        |
        +--> performance analysis
        |
        +--> cost analysis
        |
        +--> sequence analysis
        |
        +--> seasonal/time analysis
        |
        +--> chronological validation
        |
        v
Candidate hypothesis
        |
        v
Out-of-sample / stability test
        |
        +--> survives -> investigate further
        |
        +--> fails -> reject
```

The proprietary strategy core is not included in this public version.

---

# Selected Public Findings

These findings are included only to show the research process, not to advertise a trading system.

### Long-run behavior
A long XAUUSD test showed that the strategy could remain historically profitable over a very large sample, but its edge varied significantly by year and became much weaker after transaction costs.

### Regime dependence
Recent samples sometimes showed materially higher win rates than the longer historical average.

This suggested that market regime mattered more than the headline win rate.

### Time-of-day effects
Some hours showed stronger historical expectancy than the full strategy.

Instead of accepting them immediately, I compared older and newer samples to see whether the effect persisted.

### Risk
Higher percentage risk produced faster account growth in favorable periods but also created severe drawdowns.

This reinforced the distinction between:
- strategy edge,
- position sizing,
- and account survival.

---

# What I Refused To Do

I intentionally avoided several tempting shortcuts:

- treating one strong year as proof,
- optimizing many parameters at once,
- hiding losing periods,
- assuming independence without testing it,
- assuming patterns imply causation,
- ignoring spread,
- calling every profitable backtest an edge,
- and continuously changing rules until the chart looked perfect.

These decisions made the project less impressive visually, but more useful intellectually.

---

# Technical Skills Demonstrated

- Python
- pandas / NumPy
- TradingView Pine Script
- MQL5 / MT5 Expert Advisors
- Excel / XLSX data analysis
- statistical testing
- conditional probability
- expected value
- profit factor analysis
- drawdown analysis
- risk-based position sizing
- sequence analysis
- time-series segmentation
- chronological validation
- automation
- research documentation

---

# What Is Private

The following are intentionally excluded:

- exact strategy entry logic,
- exact indicator parameters,
- exact thresholds,
- exact stop-loss and take-profit rules,
- exact session filters,
- exact risk configuration,
- broker-specific execution details,
- private optimization experiments,
- raw historical datasets,
- and any proprietary signal-ranking logic.

The public project shows the **scientific process**, not the private recipe.

---

# Current Status

This research project is intentionally considered complete for now.

The final result was not:

> “I found a perfect trading strategy.”

The result was more valuable:

> **I learned how quickly a promising strategy can weaken when the sample becomes larger, costs are added, regimes are separated, and the evidence is forced to survive harder tests.**

That is the lesson I want this project to represent.

---

# Disclaimer

This repository is an educational and research portfolio project. Historical results do not guarantee future performance. It is not financial advice and does not include a production trading system.
