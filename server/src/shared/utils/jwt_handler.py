import jwt
import datetime

from config import variables


class JWTHandler:

    def __init__(self, id: int):
        self.__id = id
        self.__expiration = datetime.datetime.now() +\
            datetime.timedelta(weeks=24)

    def sign(self):
        token = jwt.encode(
            {
                'user_id': self.__id,
                'exp': self.__expiration
            },
            variables.SECRET_KEY
        )

        return token.decode('utf-8')
