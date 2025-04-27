# app/ai/keywords.py

"""
VisionBoard AI – Keyword Extraction Module

This module uses KeyBERT and a SentenceTransformer to extract the most relevant keywords from a given text.
It is optimized for fast, lightweight keyword generation within cloud-native microservices.

Functions:
    - extract_keywords(text: str, top_n: int = 5) -> List[str]
"""
# app/ai/keywords.py

from typing import List
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

# Load the sentence-transformers model once for embeddings
embedding_model: SentenceTransformer = SentenceTransformer('all-MiniLM-L6-v2')
kw_model: KeyBERT = KeyBERT(model=embedding_model)

def extract_keywords(text: str, top_n: int = 5) -> List[str]:
    """
    Extract top keywords from a given text using KeyBERT.

    Args:
        text (str): The input text to analyze.
        top_n (int): The number of top keywords to extract.

    Returns:
        List[str]: A list of extracted keywords.
    """
    # Handle empty or invalid input
    if not isinstance(text, str) or not text.strip():
        return []

    # Extract keywords with KeyBERT
    extracted = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=top_n
    )
    # Return only the keyword strings, ignoring scores
    return [keyword for keyword, _ in extracted]