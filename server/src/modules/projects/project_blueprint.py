from flask import Blueprint, request
import json

from src.modules.projects.project import Project
from src.shared.database.db import db
from src.shared.middlewares.auth_middleware import auth_middleware

project_bp = Blueprint('projects', __name__, url_prefix='/projects')


@project_bp.route('/', methods=['GET'])
@auth_middleware
def index() -> json:
    results = []
    projects = Project.query().all()

    for project in projects:
        results.append(
            {
                'id': project.id,
                'title': project.title,
                'description': project.description
            }
        )

    return json.dumps(results), 200


@project_bp.route('/', methods=['POST'])
@auth_middleware
def store() -> json:
    title, description, user_id = request.json.values()

    new_project = Project(
        title=title,
        description=description,
        user_id=user_id
    )
    db.session.add(new_project)
    db.session.commit()

    return json.dumps(
        {
            'success': f'New project created: {new_project.title}!'
        }
    ), 201
