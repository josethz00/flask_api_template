from flask import Blueprint

task = Blueprint('task', __name__, url_prefix='/task')


task.route('/', methods=['GET'])
def index():
    return 'hello'
