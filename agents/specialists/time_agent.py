from strands import Agent, tool
from agents.config import get_model
from agents.tools import get_current_time


@tool
def time_agent(query: str) -> str:
    """A specialist agent that answers questions about the current date and time.
    Delegate any time-related questions to this agent."""
    agent = Agent(
        model=get_model(),
        system_prompt="You are a time specialist. Answer questions about the current date and time concisely.",
        tools=[get_current_time],
    )
    return str(agent(query))
