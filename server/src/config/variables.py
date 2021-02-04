import os

os.environ['HOST'] = '0.0.0.0'
os.environ['PORT'] = '8080'
os.environ['DEBUG'] = 'True'
os.environ['REDIS_URL'] = 'redis://localhost:6379/0'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
REDIS_URL = os.environ.get('REDIS_URL')
