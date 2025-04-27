# app/ai/rephrase.py

"""
VisionBoard AI – Goal Rephrasing Module

 This module provides functionality to rephrase goals into more inspiring and motivational language.
 It uses a lightweight GPT-2 model to generate creative, uplifting versions of user-provided goal texts.
"""

# app/ai/rephrase.py

from transformers import pipeline
from typing import Optional

# Load GPT-2 text generation pipeline
rephrase_pipeline = pipeline(
    "text-generation",
    model="gpt2",  # Using 'gpt2' for faster, lightweight generation. Consider 'gpt2-medium' for richer outputs.
    max_length=60,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.8,  # Higher temperature encourages creativity.
)

def rephrase_goal(text: str) -> Optional[str]:
    """
    Rephrase a goal into a more inspiring and motivational sentence.

    Args:
        text (str): Original goal text.

    Returns:
        Optional[str]: Rephrased motivational text, or None if generation fails.
    """
    prompt = f"Rewrite the following goal in an inspiring, motivational tone:\n{text}\nMotivational version:"
    try:
        result = rephrase_pipeline(prompt)[0]['generated_text']
        # Extract the rephrased text cleanly
        generated = result.split("Motivational version:")[-1].strip()
        return generated
    except Exception as e:
        # Log or handle exception as needed
        return None