import json
from werkzeug.exceptions import HTTPException


def exception_handler(error: Exception) -> json:
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return json.dumps({'error': error.__repr__()}), code
