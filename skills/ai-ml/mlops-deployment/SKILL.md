---
name: mlops-deployment
description: Master model deployment, versioning, and production ML systems.
---

# MLOps & Model Deployment

## Model Serving

### Flask REST API
```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction[0]})
```

### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY model.pkl .
COPY app.py .
CMD ["python", "app.py"]
```

## MLOps Frameworks

- **MLflow**: Experiment tracking, model registry
- **Kubeflow**: ML on Kubernetes
- **DVC**: Data and model versioning
- **Weights & Biases**: Experiment tracking
- **Seldon**: Model serving platform

## ML Pipeline

```
Data → Training → Validation → Deployment → Monitoring
```

## Key Concepts

- **Model Versioning**: Track model changes
- **A/B Testing**: Compare model versions
- **Monitoring**: Performance, drift detection
- **Retraining**: Update models regularly
- **Data Pipeline**: Automated data processing
- **CI/CD for ML**: Automated model deployment

## Best Practices

✅ Version everything
✅ Automate pipelines
✅ Monitor in production
✅ Handle data drift
✅ Plan retraining
✅ Test models thoroughly
✅ Document decisions

