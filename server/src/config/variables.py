import os

os.environ['HOST'] = '0.0.0.0'
os.environ['PORT'] = '8080'
os.environ['DEBUG'] = 'True'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
