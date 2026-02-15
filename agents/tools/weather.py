import random
from strands import tool


@tool
def get_weather(location: str) -> str:
    """Returns the current weather for a given location (mock data)."""
    conditions = ["sunny", "partly cloudy", "overcast", "rainy", "snowy"]
    temp_c = random.randint(-5, 35)
    condition = random.choice(conditions)
    humidity = random.randint(30, 90)
    return (
        f"Weather in {location}: {condition}, "
        f"{temp_c}°C, humidity {humidity}%"
    )
