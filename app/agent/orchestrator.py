from app.agent.responder import create_response, create_final_response
from app.agent.executor import execute_tool_calls

def run(user_message: str) -> str:
    response = create_response(user_message)
    tool_outputs = execute_tool_calls(response)

    if tool_outputs:
        final_response = create_final_response(
            response.id,
            tool_outputs
        )
        return final_response.output_text

    return response.output_text