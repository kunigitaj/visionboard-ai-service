# VisionBoard AI Package

This directory (`app/ai/`) contains all the AI-powered modules used by the VisionBoard AI Service.

Each module is designed to be lightweight, modular, and production-ready, supporting cloud-native FastAPI endpoints.

---

## Modules Overview

| Module               | Description |
| -------------------- | ----------- |
| `summarization.py`    | Summarizes goal descriptions into concise, action-focused text (Hugging Face T5-small). |
| `sentiment.py`        | Analyzes emotional tone (positive/negative) in text (DistilBERT). |
| `keywords.py`         | Extracts keywords or key phrases from goal descriptions (KeyBERT + SentenceTransformers). |
| `predict.py`          | Predicts goal success probability based on text length using a simple linear regression model (scikit-learn). |
| `rephrase.py`         | Rewrites goal descriptions into motivational sentences (GPT-2). |

---

## Technical Stack Summary

| Task                     | Model / Library                                   | Purpose                                         |
|---------------------------|---------------------------------------------------|-------------------------------------------------|
| Summarization             | `t5-small` via Hugging Face `transformers`        | Summarize goals into clear action items         |
| Sentiment Analysis        | `distilbert-base-uncased-finetuned-sst-2-english` | Detect emotional tone of goals                  |
| Keyword Extraction        | `KeyBERT` + `all-MiniLM-L6-v2` SentenceTransformer| Extract key themes and concepts from text       |
| Progress Prediction       | `LinearRegression` (Scikit-learn)                 | Predict likelihood of goal completion           |
| Motivational Rephrasing   | `gpt2` via Hugging Face `transformers`             | Inspire by rewording goals in motivational tone |

---

## Example Usage

```python
from app.ai.summarization import summarize_text
print(summarize_text("Train for six months to run a marathon next year."))

from app.ai.sentiment import analyze_sentiment
print(analyze_sentiment("I am excited about my journey!"))

from app.ai.keywords import extract_keywords
print(extract_keywords("Learn machine learning and artificial intelligence."))

from app.ai.predict import predict_success_score
print(predict_success_score("Finish a novel", "Write 500 words a day."))

from app.ai.rephrase import rephrase_goal
print(rephrase_goal("Start running regularly."))
```

---

## Design Principles

- **Load Models Once**: Every module loads its ML model globally to optimize performance.
- **Simple, Clear Interfaces**: Plain text input and structured output.
- **Extensibility**: Easy to swap models or extend capabilities.
- **Built with Purpose**: Focused on clarity, trust, and delivering real value.

---

## License

This directory and its contents follow the VisionBoard project license:  
[Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

---
