from config import variables

class SQLConnector:

    connection_url = f'''
        {variables.SQL_DATABASE}://
        {variables.DATABASE_USER}:
        {variables.DATABASE_PASSWORD}@
        {variables.DATABASE_HOST}:
        {variables.DATABASE_PORT}/
        {variables.DATABASE_NAME}'''
