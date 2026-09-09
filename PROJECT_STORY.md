# Project Story

## From curiosity to research discipline

I started this project because I wanted to understand whether patterns in financial markets could be measured instead of guessed.

At the beginning, I was focused on finding a strategy that made money.

That goal changed.

The deeper I went into the data, the more I encountered problems that were more interesting than the original strategy:

- Why did the same rules perform differently across years?
- Why did a strong recent win rate weaken when I expanded the dataset?
- How much of an apparent edge survives transaction costs?
- When does a pattern represent information, and when is it just randomness?
- How can I test a hypothesis without accidentally fitting it to the past?
- How should risk change the interpretation of a strategy?
- Can a trading rule be automated without changing its behavior?

These questions pushed me from simple backtesting into statistics, software engineering, and research design.

## The most important failure

One of the most useful moments in the project happened when a recent period looked significantly stronger than a six-year sample.

My first instinct could have been to defend the strategy.

Instead, I treated the disagreement as evidence.

The strategy was not behaving consistently.

That changed the question from:

> Is the strategy profitable?

to:

> Under what conditions does the strategy appear to have an edge, and does that edge survive outside the period where I discovered it?

That is what led to regime analysis, seasonal analysis, time-of-day analysis, and chronological validation.

## Why failure became useful

Several filters and pattern ideas looked promising initially and then weakened when tested on unseen or older data.

Rather than hiding these results, I kept them.

They are part of the project because they show something important:

**a rejected hypothesis is still a successful experiment if the test was designed well.**

The project became less about trading and more about learning how to build evidence.

## Why I keep the core private

The exact signal rules are not public because they are part of the original research implementation.

However, hiding the core does not prevent the project from being evaluated.

The public version exposes:
- the research questions,
- validation methodology,
- analysis tools,
- experiment structure,
- technical implementation,
- and the conclusions I drew from failed and successful tests.

That is the part of the work I consider most important.
