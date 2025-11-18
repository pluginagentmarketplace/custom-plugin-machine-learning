---
name: data-science-analytics
description: Master data analysis, visualization, and insights extraction.
---

# Data Science & Analytics

## Quick Start

### Pandas Data Analysis
```python
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Explore
df.head()
df.info()
df.describe()

# Filter
df[df['age'] > 30]

# Group
df.groupby('category')['value'].sum()

# Aggregate
df.agg({'value': 'sum', 'count': 'mean'})
```

### Data Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='income')
plt.title('Age vs Income')
plt.show()
```

## Analytics Process

1. **Question Definition**: What to analyze?
2. **Data Collection**: Gather relevant data
3. **Data Cleaning**: Remove outliers, handle missing
4. **Exploration**: Understand patterns
5. **Analysis**: Statistical tests
6. **Visualization**: Create insights
7. **Communication**: Present findings

## Statistical Analysis

- **Descriptive Stats**: Mean, median, std dev
- **Hypothesis Testing**: T-tests, chi-square
- **Correlation**: Pearson, Spearman
- **Regression Analysis**: Linear, logistic

## Tools

- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Matplotlib**: Visualization
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive dashboards

## Best Practices

✅ Ask clear questions
✅ Validate assumptions
✅ Use appropriate visualizations
✅ Test hypotheses
✅ Document methodology
✅ Avoid misleading charts
✅ Cite data sources

