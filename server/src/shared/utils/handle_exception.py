import json


def handle_exception(error: Exception) -> json:
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = 'application/json'
    return response
