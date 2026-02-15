from strands import Agent
from agents.config import get_model
from agents.specialists import time_agent, weather_agent


def create_orchestrator() -> Agent:
    """Build and return the orchestrator agent with all specialist tools."""
    return Agent(
        model=get_model(),
        system_prompt=(
            "You are an orchestrator that delegates to specialist agents. "
            "Use 'time_agent' for date/time questions and 'weather_agent' for weather questions. "
            "For queries that span multiple topics, call each relevant specialist. "
            "Combine the specialist responses into a single concise answer."
        ),
        tools=[time_agent, weather_agent],
    )
