import os
from strands.models.bedrock import BedrockModel

# --- Option A: Bedrock (active) ---
# Uses the Lambda's IAM role for auth — no API key needed.

def get_model():
    return BedrockModel(
        model_id=os.environ.get("BEDROCK_MODEL_ID", "us.anthropic.claude-sonnet-4-20250514-v1:0"),
    )

# --- Option B: Anthropic direct (commented out) ---
# Requires ANTHROPIC_API_KEY env var.
#
# from strands.models.anthropic import AnthropicModel
#
# def get_model():
#     return AnthropicModel(
#         client_args={"api_key": os.environ["ANTHROPIC_API_KEY"]},
#         model_id=os.environ.get("ANTHROPIC_MODEL_ID", "claude-sonnet-4-20250514"),
#     )
