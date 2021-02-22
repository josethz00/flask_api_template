from functools import wraps
from flask import request
from config import variables
import jwt
from jwt.exceptions import (
    DecodeError,
    InvalidTokenError,
    InvalidSignatureError
)


def auth_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers['authorization']
        if not token:
            raise InvalidTokenError('Invalid token')
        parts = token.split(' ')
        if len(parts) > 2:
            raise InvalidTokenError('Invalid token')
        [scheme, token] = parts
        if scheme.strip() != 'Bearer':
            raise InvalidSignatureError('Invalid token signature')
        try:
            jwt.decode(token, variables.SECRET_KEY)
            return func(*args, **kwargs)
        except DecodeError:
            raise DecodeError('Token could not be decoded')
    return decorated_function
