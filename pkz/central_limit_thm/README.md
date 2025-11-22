# Central Limit Theorem (CLT)

The Central Limit Theorem (CLT) is one of the most important concepts in statistics, and it plays a significant role in data science and machine learning. However, it's sometimes misunderstood, leading to the misconception that any dataset will become normally distributed as its size increases, which is incorrect.

The key idea behind the CLT is that the sum (or mean) of samples will become a normal distribution as the number of measurements increases, regardless of the sample size or original distribution of the data.

To visualize this concept, I performed an experiment to observe how the distribution changes as the sample size increases. You'll see that the size of the data itself has no effect on transforming the distribution. Only the mean of the samples converges to a normal distribution as the number of measurements increases.

## Getting Started
```bash
# Install dependencies (using uv)
uv sync

# Run the app
uv run streamlit run pkz/central_limit_thm/app.py
```
