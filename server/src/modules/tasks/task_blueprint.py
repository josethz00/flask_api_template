from flask import Blueprint, request
import json

from src.modules.tasks.task import Task
from src.shared.database.db import db
from src.shared.middlewares.auth_middleware import auth_middleware

task_bp = Blueprint('task', __name__, url_prefix='/tasks')


@task_bp.route('/', methods=['GET'])
@auth_middleware
def index() -> json:
    results = []
    tasks = Task.query().all()

    for task in tasks:
        results.append(
            {
                'id': task.id,
                'title': task.title,
                'description': task.description
            }
        )

    return json.dumps(results), 200


@task_bp.route('/', methods=['POST'])
@auth_middleware
def store() -> json:
    title, description, priority, user_id, project_id = request.json.values()

    new_task = Task(
        title=title,
        description=description,
        priority=priority,
        user_id=user_id,
        project_id=project_id
    )
    db.session.add(new_task)
    db.session.commit()

    return json.dumps(
        {
            'success': f'New task created: {new_task.title}!'
        }
    ), 201
