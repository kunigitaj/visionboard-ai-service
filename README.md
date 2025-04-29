# VisionBoard AI Service

![Node.js](https://img.shields.io/badge/Node.js-18.x-green)  
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey)

VisionBoard AI Service empowers users to expand, motivate, and predict goal success through cutting-edge AI-powered APIs.  
Leveraging state-of-the-art NLP and predictive modeling, this cloud-native microservice suite transforms simple goal descriptions into actionable plans, insightful sentiments, relevant keywords, and success predictions—all designed to inspire and guide personal growth.

Designed for clarity, scalability, and real-world impact, VisionBoard bridges AI technology and meaningful user experiences.

---

## Architecture Overview

VisionBoard AI Service is composed of modular microservices, each responsible for a core AI function:

- **Goal Expansion Module**: Transforms brief goals into detailed, motivational plans using GPT-2 Large.
- **Sentiment Analysis Module**: Detects emotional tone with MiniLM-based classifiers.
- **Keyword Extraction Module**: Identifies key themes via KeyBERT.
- **Progress Prediction Module**: Predicts goal completion likelihood using Scikit-learn models.
- **Goal Rephrasing Module**: Enhances motivation by rewriting goals in inspiring tones.

Each module communicates via RESTful APIs, allowing independent scaling and easy integration.

---

## Built With

- **FastAPI** – High-performance Python API framework  
- **Hugging Face Transformers** – GPT-2 Large, MiniLM for NLP tasks  
- **KeyBERT** – Keyword extraction using BERT embeddings  
- **Scikit-learn** – Predictive modeling  
- **Docker** – Containerization for deployment  
- **Uvicorn** – ASGI server for high-performance serving  

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
- _Expands a short goal description into a detailed, motivational step-by-step plan._

**Example Request:**

```bash
curl -X POST http://localhost:8000/generate_goal_plan \
-H "Content-Type: application/json" \
-d '{"text": "Run a marathon"}'
```

---

### 2. Sentiment Analysis API

- **Endpoint**: `POST /sentiment`  
- _Analyzes emotional tone (positive/negative) in goal descriptions._

**Example Request:**

```bash
curl -X POST http://localhost:8000/sentiment \
-H "Content-Type: application/json" \
-d '{"text": "I am really excited about starting my new fitness journey!"}'
```

---

### 3. Keyword Extraction API

- **Endpoint**: `POST /keywords`  
- _Extracts key themes or concepts from a goal description._

**Example Request:**

```bash
curl -X POST http://localhost:8000/keywords \
-H "Content-Type: application/json" \
-d '{"text": "Learn machine learning and artificial intelligence concepts."}'
```

---

### 4. Progress Prediction API

- **Endpoint**: `POST /predict`  
- _Predicts the likelihood of completing a goal based on text metadata._

**Example Request:**

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"title": "Finish a novel", "description": "Write 500 words every day for the next 6 months."}'
```

---

### 5. Goal Rephrasing API

- **Endpoint**: `POST /rephrase`  
- _Rewrites goal descriptions into motivational, inspiring tones._

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

Quickly test VisionBoard AI Service's capabilities:

### Goal Expansion & Motivation

```bash
# Expand a Goal into a Detailed Plan
curl -X POST http://localhost:8000/generate_goal_plan \
-H "Content-Type: application/json" \
-d '{"text": "Run a marathon"}'

# Rephrase a Goal to be More Motivating
curl -X POST http://localhost:8000/rephrase \
-H "Content-Type: application/json" \
-d '{"text": "Start exercising regularly to improve health."}'
```

### Sentiment Analysis & Keyword Extraction

```bash
# Analyze Sentiment of a Goal
curl -X POST http://localhost:8000/sentiment \
-H "Content-Type: application/json" \
-d '{"text": "I am excited to start my journey of learning new skills!"}'

# Extract Keywords from a Goal
curl -X POST http://localhost:8000/keywords \
-H "Content-Type: application/json" \
-d '{"text": "Learn Python programming, data science, and machine learning."}'
```

### Progress Prediction

```bash
# Predict Goal Completion Likelihood
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"title": "Write a technical blog", "description": "Publish one new blog post every week for six months."}'
```

---

## VisionBoard AI Service: At a Glance

- **Purpose**: Expand, motivate, and predict goal success through AI-powered APIs.  
- **Tech Stack**: FastAPI · Hugging Face Transformers (GPT-2 Large, MiniLM) · KeyBERT · Scikit-learn · Docker  
- **Style**: Cloud-native, modular, lightweight microservices  
- **Impact**: Empowers smarter, more inspiring personal growth journeys

---

## License

The content and source code in this project are the intellectual property of Kunigitaj.  
Unauthorized reproduction, modification, distribution, or commercial use without express permission is prohibited.

This work is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

You may remix, adapt, and build upon this work non-commercially, provided you credit Kunigitaj and license your new creations under identical terms.

---

## Special Thanks

- **Hugging Face**  
- **KeyBERT**  
- **Scikit-learn**  
- **FastAPI**

---