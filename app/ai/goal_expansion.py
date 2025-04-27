# app/ai/goal_expansion.py

"""
VisionBoard AI – Goal Expansion Module

Transforms a short user goal input into a detailed, motivational, and actionable step-by-step guide
using high-quality, instruction-tuned text generation models.

Powered by Hugging Face Transformers (GPT-2 Large).
"""

from transformers import pipeline

# Load text generation model at module level
generator = pipeline(
    "text-generation",
    model="gpt2-large",
    max_new_tokens=250,
    num_return_sequences=1,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.2,
    do_sample=True,
)

def generate_goal_plan(text: str) -> str:
    """
    Generates a detailed, motivational, and actionable plan from a short user-provided goal using AI text generation.
    """
    if not text or len(text.strip()) < 5:
        return "Please provide a more meaningful goal to expand."

    text = text.strip()

    prompt = (
        f"Expand the goal '{text}' into exactly 5 smart, specific, and motivational steps.\n"
        "Each step must start with 'Step X:' and focus on preparation, action, and results.\n"
        "Make it sound clear, inspiring, and practical.\n"
        "Example:\n"
        "Goal: Learn Python\n"
        "Step 1: Research beginner-friendly Python courses that align with your interests.\n"
        "Step 2: Install Python and set up a simple coding environment on your laptop.\n"
        "Step 3: Dedicate 30 minutes daily to small hands-on coding exercises.\n"
        "Step 4: Build a mini project (e.g., a to-do list app) to apply what you've learned.\n"
        "Step 5: Share your project on GitHub or a community to get feedback and stay motivated.\n\n"
        f"Goal: {text}\n"
    )

    try:
        result = generator(prompt)[0]['generated_text']
        expanded = result.split(f"Goal: {text}")[-1].strip()
        expanded = expanded.split('Goal:')[0].strip()
        return expanded
    except Exception as e:
        return f"Expansion error: {str(e)}"