from datetime import datetime, timezone
from strands import tool


@tool
def get_current_time() -> str:
    """Returns the current UTC date and time."""
    now = datetime.now(timezone.utc).isoformat()
    return f"The current UTC date and time is {now}"
