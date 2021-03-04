from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from flask_mail import Mail

from src.shared.utils.exception_handler import exception_handler
from src.modules.projects.project_blueprint import project_bp
from src.modules.users.user_blueprint import user_bp
from src.modules.tasks.task_blueprint import task_bp
from src.shared.database.sql_connector import SQLConnector
from src.shared.database.db import db
from config import variables, extensions
import manage


def create_app() -> Flask:

    app = Flask(__name__)
    db_conn = SQLConnector()

    configure_cors(app, extensions.cors)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_conn.connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['MAIL_SERVER'] = variables.MAIL_SERVER
    app.config['MAIL_PORT'] = variables.MAIL_PORT
    app.config['MAIL_USERNAME'] = variables.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = variables.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = variables.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = variables.MAIL_USE_SSL

    db.init_app(app)
    with app.app_context():
        db.create_all()

    configure_mail(app, extensions.mail)

    app.register_blueprint(user_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(task_bp)

    @app.errorhandler(Exception)
    def get_error(error):
        return exception_handler(error)

    return app


def configure_mail(app: Flask, mail: Mail) -> None:
    mail.init_app(app)


def configure_cors(app: Flask, cors: CORS) -> None:
    cors.init_app(app)
