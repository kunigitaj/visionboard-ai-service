# app/ai/sentiment.py

"""
VisionBoard AI – Sentiment Analysis Module

This module provides functionality to analyze the emotional tone of a given text 
using a pre-trained DistilBERT model fine-tuned for sentiment classification.

Capabilities:
- Analyze short or long goal descriptions.
- Classify text as POSITIVE or NEGATIVE sentiment.
- Lightweight and fast for real-time microservice deployments.
"""

from transformers import pipeline
from typing import Literal

# Load the sentiment analysis pipeline once at module level
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text: str) -> Literal["POSITIVE", "NEGATIVE"]:
    """
    Analyze the sentiment of a given text input.

    Args:
        text (str): The input text to analyze.

    Returns:
        Literal["POSITIVE", "NEGATIVE"]: Detected sentiment label.
    """
    try:
        result = sentiment_pipeline(text)[0]  # Pipeline returns a list of results
        return result['label']  # Expected: 'POSITIVE' or 'NEGATIVE'
    except Exception as e:
        # Fallback in case model inference fails
        return "NEGATIVE"