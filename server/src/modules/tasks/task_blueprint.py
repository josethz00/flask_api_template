from flask import Blueprint

task_bp = Blueprint('task', __name__, url_prefix='/task')


task_bp.route('/', methods=['GET'])
def index():
    return 'hello'
