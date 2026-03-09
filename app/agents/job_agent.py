"""
job_agent.py
"""

import os
import json
import re
from groq import Groq
from app.services.prompt_templates import JOB_AGENT_PROMPT


class JobAgent:

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"

    def analyze_job_request(self, user_query: str, search_queries: list):

        formatted_queries = "\n".join(search_queries)

        prompt = JOB_AGENT_PROMPT.format(
            user_query=user_query,
            queries=formatted_queries
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI job assistant that always returns valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=200
        )

        result = response.choices[0].message.content

        parsed = {}

        try:
            # Try direct JSON parse
            parsed = json.loads(result)

        except:

            # Extract JSON block if extra text exists
            match = re.search(r"\{.*\}", result, re.DOTALL)

            if match:
                try:
                    parsed = json.loads(match.group())
                except:
                    parsed = {"raw_output": result}

            else:
                parsed = {"raw_output": result}

        return {
            "user_query": user_query,
            "analysis": parsed,
            "queries_used": search_queries
        }