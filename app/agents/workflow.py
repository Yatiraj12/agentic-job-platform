"""
workflow.py

Orchestrates the agent workflow for the Job Search Agent system.
"""

from app.services.query_generator import generate_search_queries
from app.agents.job_agent import JobAgent


class JobSearchWorkflow:
    """
    Coordinates the end-to-end workflow of the job search agent.
    """

    def __init__(self):
        self.agent = JobAgent()

    def run(self, user_query: str):
        """
        Runs the full job search agent pipeline.

        Steps:
        1. Generate job search queries
        2. Run AI agent reasoning
        3. Return structured result

        Args:
            user_query (str): user's job search request

        Returns:
            dict: structured agent output
        """

        # Step 1: Generate search queries
        search_queries = generate_search_queries(user_query)

        # Step 2: Agent reasoning
        agent_result = self.agent.analyze_job_request(
            user_query,
            search_queries
        )

        # Step 3: Return combined result
        return {
            "status": "success",
            "input": user_query,
            "generated_queries": search_queries,
            "agent_output": agent_result
        }