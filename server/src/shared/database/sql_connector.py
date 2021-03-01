from config import variables


class SQLConnector:

    def __init__(self):
        self.connection_url = f'{variables.SQL_DATABASE}://'\
            f'{variables.DATABASE_USER}:'\
            f'{variables.DATABASE_PASSWORD}@'\
            f'{variables.DATABASE_HOST}:'\
            f'{variables.DATABASE_PORT}/'\
            f'{variables.DATABASE_NAME}'
