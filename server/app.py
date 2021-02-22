from flask import Flask
from src.shared.utils.exception_handler import exception_handler
from src.modules.projects.project_blueprint import project_bp
from src.modules.users.user_blueprint import user_bp
from src.modules.tasks.task_blueprint import task_bp


def create_app() -> Flask:

    app = Flask(__name__)
    db_conn = SQLConnector()

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(task_bp)

    @app.errorhandler(Exception)
    def get_error(error):
        return exception_handler(error)

    return app
