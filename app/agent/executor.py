import json
from app.tools.expenses import add_expense, get_expenses

TOOL_FUNCTIONS = {
    "add_expense": add_expense,
    "get_expenses": get_expenses,
}

def run(tool_name: str, tool_arguments: dict):
    if tool_name not in TOOL_FUNCTIONS:
        return "Unknown tool"

    tool_function = TOOL_FUNCTIONS[tool_name]
    return tool_function(**tool_arguments)

def execute_tool_calls(response):
    tool_outputs = []
    for item in response.output:
        if item.type == "function_call":
            arguments = json.loads(item.arguments)
            tool_result = run(item.name, arguments)
            tool_outputs.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": str(tool_result)
            })

    return tool_outputs