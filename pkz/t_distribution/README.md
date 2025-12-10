# T-Distribution Visualization

An interactive Streamlit app that visualizes the relationship between the t-distribution and the standard normal distribution.

## Overview

This application demonstrates a fundamental concept in statistics: how the **t-distribution converges to the standard normal distribution** as the degrees of freedom (sample size) increases.

## Features

- **Interactive Slider**: Adjust the degrees of freedom from 1 to 100
- **Dual Visualization**: Compare t-distribution (red) with standard normal distribution (blue)

## What You'll Learn

1. **Visual Convergence**: See how the t-distribution's shape changes as sample size increases
2. **Heavy Tails**: Observe that t-distributions have heavier tails for small sample sizes
3. **Practical Threshold**: Understand why df ≥ 30 is often considered "large enough" for normal approximation

## Running the App

### Prerequisites

Ensure you have `uv` installed and dependencies synced:

```bash
uv sync
```

### Launch the App

From the project root directory:

```bash
uv run streamlit run pkz/t_distribution/app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## Key Concepts

### Degrees of Freedom (df)

- **Definition**: df = n - 1, where n is the sample size
- **Impact**: As df increases, the t-distribution approaches the normal distribution
- **Small samples** (df < 30): Use t-distribution for more conservative estimates
- **Large samples** (df ≥ 30): T-distribution ≈ Normal distribution

### When to Use Which Distribution

| Scenario | Distribution | Reason |
|----------|--------------|--------|
| Small sample, unknown σ | T-distribution | Accounts for additional uncertainty |
| Large sample (n ≥ 30) | Either | Distributions are nearly identical |
| Known population σ | Normal | No need for t-distribution adjustment |
