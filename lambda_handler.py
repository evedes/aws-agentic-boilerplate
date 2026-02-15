import json
from agents import create_orchestrator


def handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")
        query = body.get("query")
        if not query:
            return {"statusCode": 400, "body": json.dumps({"error": "missing 'query' field"})}
        orchestrator = create_orchestrator()
        result = orchestrator(query)
        return {"statusCode": 200, "body": json.dumps({"answer": str(result)})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
