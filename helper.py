def chat_agent_response_template(data):
    chat_agent_response = {
        "message": data["message"],
        "status": data["status_code"],
        "input": data["prompt"],
        "output": data["map_competency_questions"]
    }

    return chat_agent_response

def response_template(data):
    response = {
        "message": data["message"],
        "status": data["status_code"],
        "data": data["data"]
    }

    return response
