# VisionBoard AI Service

![Node.js](https://img.shields.io/badge/Node.js-18.x-green) 
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey)

VisionBoard AI Service enhances goal tracking through intelligent, cloud-native microservices powered by open-source AI models.

Designed to showcase full-stack AI architecture skills — from NLP to prediction modeling — this project bridges technology and real-world outcomes with clarity, trust, and purpose.

---

## Why This Project Matters

- **Real-World Utility**: Practical APIs to enrich goal setting and personal growth applications.
- **Cloud-Native Design**: Built to run as lightweight, scalable microservices.
- **Modern AI Usage**: Combines NLP, sentiment analysis, predictive modeling, and text generation.
- **Production-Ready**: Dockerized, documented, and easily extendable for real-world deployment.

---

## Built With

- **FastAPI** – high-performance Python API framework
- **Hugging Face Transformers** – NLP models (T5, DistilBERT, GPT-2)
- **KeyBERT** – keyword extraction
- **Scikit-learn** – predictive modeling
- **Docker** – containerization ready
- **Uvicorn** – ASGI server

---

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API service locally
uvicorn app.main:app --reload
```

Access the API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Documentation

### 1. Goal Expansion API

- **Endpoint**: `POST /generate_goal_plan`
- **Description**: Expands a short goal description into a detailed, motivational step-by-step plan to guide achievement.

**Example Request:**
```bash
curl -X POST http://localhost:8000/generate_goal_plan \
-H "Content-Type: application/json" \
-d '{"text": "Run a marathon"}'
```

---

### 2. Goal Sentiment Analysis API

- **Endpoint**: `POST /sentiment`
- **Description**: Detects emotional tone (positive/negative) in goal descriptions.

**Example Request:**
```bash
curl -X POST http://localhost:8000/sentiment \
-H "Content-Type: application/json" \
-d '{"text": "I am really excited about starting my new fitness journey!"}'
```

---

### 3. Goal Tagging (Keyword Extraction API)

- **Endpoint**: `POST /keywords`
- **Description**: Extracts key themes or concepts from a goal description.

**Example Request:**
```bash
curl -X POST http://localhost:8000/keywords \
-H "Content-Type: application/json" \
-d '{"text": "Learn machine learning and artificial intelligence concepts."}'
```

---

### 4. Vision Progress Prediction API

- **Endpoint**: `POST /predict`
- **Description**: Predicts the likelihood of completing a goal based on text metadata.

**Example Request:**
```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"title": "Finish a novel", "description": "Write 500 words every day for the next 6 months."}'
```

---

### 5. Goal Rephrasing for Motivation API

- **Endpoint**: `POST /rephrase`
- **Description**: Rewrites goal descriptions into motivational, inspiring tones.

**Example Request:**
```bash
curl -X POST http://localhost:8000/rephrase \
-H "Content-Type: application/json" \
-d '{"text": "Start running regularly."}'
```

---

## Interactive API Explorer

FastAPI automatically generates an interactive API explorer:

- [Swagger UI Documentation](http://localhost:8000/docs)

Explore endpoints, test APIs, and review expected inputs and outputs directly in your browser.

---

## Demo Commands

Quickly test the APIs locally with these examples:

```bash
# 1. Expand a Goal
curl -X POST http://localhost:8000/generate_goal_plan \
-H "Content-Type: application/json" \
-d '{"text": "Run a marathon"}'

# 2. Analyze Sentiment of a Goal
curl -X POST http://localhost:8000/sentiment \
-H "Content-Type: application/json" \
-d '{"text": "I am excited to start my journey of learning new skills!"}'

# 3. Extract Keywords from a Goal
curl -X POST http://localhost:8000/keywords \
-H "Content-Type: application/json" \
-d '{"text": "Learn Python programming, data science, and machine learning."}'

# 4. Predict Goal Completion Likelihood
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"title": "Write a technical blog", "description": "Publish one new blog post every week for six months."}'

# 5. Rephrase a Goal to be More Motivating
curl -X POST http://localhost:8000/rephrase \
-H "Content-Type: application/json" \
-d '{"text": "Start exercising regularly to improve health."}'
```

Each command **showcases** a key AI-powered feature of the VisionBoard AI Service.

---

## VisionBoard AI Service: At a Glance

- **Purpose**: Expand, motivate, and predict goal success using AI-powered APIs.
- **Tech Stack**: FastAPI · Hugging Face · KeyBERT · Scikit-learn · Docker
- **Style**: Cloud-native, modular, lightweight microservices.
- **Impact**: Empowers smarter, more inspiring personal growth journeys.

---

## License

The content and source code in this project are the intellectual property of Kunigitaj. Unauthorized reproduction, modification, or distribution without express permission is strictly prohibited.

This work is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/), allowing non-commercial use with attribution.

Users are free to remix, adapt, and build upon this work non-commercially, provided they credit Kunigitaj and license their new creations under identical terms.

---

## Special Thanks

- Hugging Face
- KeyBERT
- Scikit-learn
- FastAPI

---