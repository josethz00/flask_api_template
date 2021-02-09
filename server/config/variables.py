import os

os.environ['HOST'] = '0.0.0.0'
os.environ['PORT'] = '8080'
os.environ['DEBUG'] = 'True'
os.environ['REDIS_URL'] = 'redis://localhost:6379/0'
os.environ['SQL_DATABASE'] = 'postgresql'
os.environ['DATABASE_USER'] = 'postgres'
os.environ['DATABASE_PASSWORD'] = 'docker'
os.environ['DATABASE_DATABASE'] = 'flask_tutorial'
os.environ['DATABASE_HOST'] = 'localhost'
os.environ['DATABASE_PORT'] = '5433'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
REDIS_URL = os.environ.get('REDIS_URL')
SQL_DATABASE = os.environ.get('SQL_DATABASE')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_DATABASE = os.environ.get('DATABASE_DATABASE')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
