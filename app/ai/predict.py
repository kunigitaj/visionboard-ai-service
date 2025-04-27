# app/ai/predict.py

"""
VisionBoard AI – Predict goal success likelihood using semantic embeddings.

This module trains a lightweight linear regression model based on
sentence embeddings of goal titles and descriptions, enabling
realistic success score predictions for goal tracking applications.
"""

from sklearn.linear_model import LinearRegression
from sentence_transformers import SentenceTransformer
import numpy as np

# Mini realistic dataset (title, description, success probability %)
TRAINING_DATA = [
    ("Start jogging", "Run for 15 minutes every day for 6 months.", 85),
    ("Build an app", "Launch MVP for startup idea in 4 months.", 50),
    ("Write a novel", "Write 1 chapter per week for 12 months.", 65),
    ("Learn Python", "Complete 2 coding projects and 1 certification.", 90),
    ("Lose weight", "Lose 20 pounds by maintaining diet and exercise.", 75),
    ("Start meditation", "Practice mindfulness for 10 minutes daily.", 80),
    ("Publish blog", "Write and publish 12 articles over the next year.", 60),
    ("Prepare for certification", "Study for and pass AWS Solutions Architect exam.", 85),
    ("Learn Spanish", "Practice Spanish daily for 30 minutes for 8 months.", 70),
    ("Finish online course", "Complete a machine learning course within 3 months.", 88),
]

# Initialize the embedder
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def train_prediction_model() -> LinearRegression:
    """Train and return a success prediction model based on goal embeddings."""
    texts = [f"{title} {desc}" for (title, desc, _) in TRAINING_DATA]
    X_train = embedder.encode(texts)
    y_train = np.array([score for (_, _, score) in TRAINING_DATA])
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Train the model when module loads
model = train_prediction_model()

def predict_success_score(title: str, description: str) -> int:
    """
    Predict the likelihood of goal success based on title and description embeddings.
    
    Args:
        title (str): The goal title.
        description (str): The goal description.

    Returns:
        int: Predicted success score between 0 and 100.
    """
    text = f"{title} {description}"
    embedding = embedder.encode([text])
    prediction = model.predict(embedding)[0]
    return int(np.clip(prediction, 0, 100))