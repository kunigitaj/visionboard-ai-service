# app/main.py

# --- Third-Party Imports ---
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- Internal Imports ---
from app.ai.goal_expansion import generate_goal_plan
from app.ai.keywords import extract_keywords
from app.ai.sentiment import analyze_sentiment
from app.ai.predict import predict_success_score
from app.ai.rephrase import rephrase_goal

# --- OpenAPI Tags Metadata ---
tags_metadata = [
    {
        "name": "Goal Expansion",
        "description": "Expand short goals into detailed, motivational plans.",
    },
    {
        "name": "Goal Analysis",
        "description": "Analyze goals by extracting keywords, sentiment, and predicting success.",
    },
    {
        "name": "Goal Enhancement",
        "description": "Enhance goals by rephrasing them into motivational versions.",
    },
    {
        "name": "Health",
        "description": "Service health checks to verify availability.",
    },
]

# --- App Initialization ---
app = FastAPI(
    title="VisionBoard AI Service",
    description="Microservice providing AI-powered goal enhancements for goal setting, tracking, and motivation.",
    version="1.0.0",
    openapi_tags=tags_metadata,
)

# --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # TODO: Update allowed origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Request Models ---
class GoalExpansionRequest(BaseModel):
    text: str

class KeywordsRequest(BaseModel):
    text: str
    top_n: int = 5

class SentimentRequest(BaseModel):
    text: str

class PredictionRequest(BaseModel):
    title: str
    description: str

class RephraseRequest(BaseModel):
    text: str

# --- Response Models ---
class GoalExpansionResponse(BaseModel):
    plan: str

    class Config:
        schema_extra = {
            "example": {
                "plan": "1. Break the goal into actionable steps. 2. Set a timeline. 3. Stay motivated by celebrating small wins."
            }
        }

class KeywordsResponse(BaseModel):
    keywords: list[str]

    class Config:
        schema_extra = {
            "example": {
                "keywords": ["fitness", "routine", "motivation"]
            }
        }

class SentimentResponse(BaseModel):
    sentiment: str

    class Config:
        schema_extra = {
            "example": {
                "sentiment": "positive"
            }
        }

# Consistent HealthCheck response model
class HealthCheckResponse(BaseModel):
    status: str

    class Config:
        schema_extra = {
            "example": {
                "status": "VisionBoard AI Service is running"
            }
        }

class PredictionResponse(BaseModel):
    score: int

    class Config:
        schema_extra = {
            "example": {
                "score": 87
            }
        }

class RephraseResponse(BaseModel):
    rephrased: str

    class Config:
        schema_extra = {
            "example": {
                "rephrased": "I am committed to building a healthy, energizing fitness routine that empowers me every day."
            }
        }

# --- API Routes ---
@app.get("/healthz", tags=["Health"], response_model=HealthCheckResponse)
def health_check() -> HealthCheckResponse:
    """Health check endpoint to verify VisionBoard AI Service is running."""
    return HealthCheckResponse(status="VisionBoard AI Service is running")

@app.post("/generate_goal_plan", tags=["Goal Expansion"], response_model=GoalExpansionResponse)
def expand_goal_plan(request: GoalExpansionRequest) -> GoalExpansionResponse:
    """Expand a short user goal into a detailed, motivational plan."""
    expanded_plan = generate_goal_plan(request.text)
    return GoalExpansionResponse(plan=expanded_plan)

@app.post("/keywords", tags=["Goal Analysis"], response_model=KeywordsResponse)
def extract_goal_keywords(request: KeywordsRequest) -> KeywordsResponse:
    """Extract key concepts and topics from a goal description."""
    keywords = extract_keywords(request.text, top_n=request.top_n)
    return KeywordsResponse(keywords=keywords)

@app.post("/sentiment", tags=["Goal Analysis"], response_model=SentimentResponse)
def analyze_goal_sentiment(request: SentimentRequest) -> SentimentResponse:
    """Analyze the emotional sentiment (Positive/Negative) of a goal."""
    sentiment = analyze_sentiment(request.text)
    return SentimentResponse(sentiment=sentiment)

@app.post("/predict", tags=["Goal Analysis"], response_model=PredictionResponse)
def predict_goal_success_score(request: PredictionRequest) -> PredictionResponse:
    """Predict the likelihood of successfully achieving a goal."""
    score = predict_success_score(request.title, request.description)
    return PredictionResponse(score=score)

@app.post("/rephrase", tags=["Goal Enhancement"], response_model=RephraseResponse)
def rephrase_goal_text(request: RephraseRequest) -> RephraseResponse:
    """Rewrite a goal into a more motivational and inspiring version."""
    rephrased = rephrase_goal(request.text)
    return RephraseResponse(rephrased=rephrased)