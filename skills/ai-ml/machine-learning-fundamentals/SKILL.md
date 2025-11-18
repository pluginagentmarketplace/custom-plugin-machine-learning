---
name: machine-learning-fundamentals
description: Master ML fundamentals, algorithms, and best practices.
---

# Machine Learning Fundamentals

## Quick Start

### Linear Regression
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 5, 4])

model = LinearRegression()
model.fit(X, y)
predictions = model.predict([[5]])
```

### Classification
```python
from sklearn.tree import DecisionTreeClassifier

X = [[0, 0], [1, 1]]
y = [0, 1]

clf = DecisionTreeClassifier()
clf.fit(X, y)
clf.predict([[2, 2]])
```

## ML Workflow

1. **Data Collection**: Gather training data
2. **Preprocessing**: Clean, normalize, split
3. **Feature Engineering**: Select/create features
4. **Model Selection**: Choose algorithm
5. **Training**: Fit model to data
6. **Evaluation**: Assess performance
7. **Hyperparameter Tuning**: Optimize
8. **Deployment**: Put model in production

## Key Algorithms

- **Regression**: Linear, polynomial, ridge
- **Classification**: Logistic, SVM, Random Forest
- **Clustering**: K-means, hierarchical
- **Ensemble**: Gradient Boosting, Random Forest

## Evaluation Metrics

- **Regression**: MSE, RMSE, R²
- **Classification**: Accuracy, Precision, Recall, F1
- **Clustering**: Silhouette score, Davies-Bouldin

## Best Practices

✅ Always split train/test data
✅ Scale/normalize features
✅ Handle missing values
✅ Avoid overfitting
✅ Cross-validate
✅ Use appropriate metrics
✅ Document experiments

