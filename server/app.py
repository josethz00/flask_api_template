from flask import Flask
from flask_cors import CORS
from celery import Celery
from werkzeug.exceptions import HTTPException

from src.shared.utils.handle_exception import handle_exception
from src.modules.projects.project_blueprint import project_bp
from src.modules.users.user_blueprint import user_bp
from src.modules.tasks.task_blueprint import task_bp
from config import variables

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(project_bp)
app.register_blueprint(task_bp)

app.config['CELERY_BROKER_URL'] = variables.REDIS_URL
app.config['CELERY_RESULT_BACKEND'] = variables.REDIS_URL

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.errorhandler(HTTPException)
def get_error(error):
    return handle_exception(error)


if __name__ == '__main__':
    app.run(
        host=variables.HOST,
        port=variables.PORT,
        debug=bool(variables.DEBUG)
    )
