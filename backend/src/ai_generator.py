import os
import json
from openai import OpenAI
from typing import Dict, Any

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert coding challenge creator. 
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer.
    """
    
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in generating multiple-choice questions."
                },
                {
                    "role": "user",
                    "content": f"Generate a {difficulty} level multiple-choice question with 4 options and provide the correct answer."
                }
            ],
            max_tokens=150
        )

        content = response.choices[0].message.content.strip()
        # Assuming the content is structured as JSON
        challenge_data = json.loads(content)

        return challenge_data

    except Exception as e:
        raise RuntimeError(f"Failed to generate challenge: {str(e)}")