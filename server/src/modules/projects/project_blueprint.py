from flask import Blueprint

project_bp = Blueprint('projects', __name__, url_prefix='/projects')


project_bp.route('/', methods=['GET'])
def index():
    return 'hello'
