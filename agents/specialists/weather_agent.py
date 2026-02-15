from strands import Agent, tool
from agents.config import get_model
from agents.tools import get_weather


@tool
def weather_agent(query: str) -> str:
    """A specialist agent that answers questions about weather conditions for any location.
    Delegate any weather-related questions to this agent."""
    agent = Agent(
        model=get_model(),
        system_prompt="You are a weather specialist. Answer questions about weather conditions concisely.",
        tools=[get_weather],
    )
    return str(agent(query))
