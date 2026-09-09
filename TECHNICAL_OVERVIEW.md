# Technical Overview

## Python

Python was used for:
- XLSX/CSV parsing,
- trade cleaning,
- conditional probability analysis,
- sequence scanning,
- seasonal/time segmentation,
- yearly performance analysis,
- cost sensitivity,
- and automated report generation.

## Pine Script

TradingView Pine Script was used for:
- strategy prototyping,
- historical backtesting,
- trade generation,
- and parameter-controlled experiments.

## MQL5

The MT5 Expert Advisor implementation included:
- closed-candle signal evaluation,
- indicator handles,
- order placement,
- stop-loss and take-profit handling,
- dynamic risk-based lot sizing,
- one-position controls,
- and Strategy Tester compatibility.

## Statistical concepts used

- probability
- conditional probability
- expected value
- break-even probability
- variance awareness
- z-scores
- confidence intervals
- profit factor
- drawdown
- streak analysis
- chronological validation
- multiple-testing awareness

## Engineering principle

Research code and execution code were kept conceptually separate.

The goal was to prevent an exploratory analysis tool from silently changing the rules of the execution system.
