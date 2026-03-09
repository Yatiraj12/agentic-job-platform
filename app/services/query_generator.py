"""
query_generator.py

Generates optimized job search queries using Groq LLM.
"""

import os
from dotenv import load_dotenv
from groq import Groq
from app.services.prompt_templates import QUERY_GENERATION_PROMPT

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.3-70b-versatile"


def generate_search_queries(user_query: str):
    """
    Generate optimized job search queries from a user request.

    Args:
        user_query (str): User's job search request

    Returns:
        list: list of generated job search queries
    """

    prompt = QUERY_GENERATION_PROMPT.format(
        user_query=user_query
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You generate job search queries."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    result_text = response.choices[0].message.content

    queries = [
        q.strip("- ").strip()
        for q in result_text.split("\n")
        if q.strip()
    ]

    return queries