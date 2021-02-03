from flask import Flask
from flask_cors import CORS
from celery import Celery
from src.config import variables

app = Flask(__name__)
CORS(app)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

if __name__ == '__main__':
    print('Server is running right now...')
    app.run(
        host=variables.HOST,
        port=variables.PORT,
        debug=bool(variables.DEBUG)
    )
