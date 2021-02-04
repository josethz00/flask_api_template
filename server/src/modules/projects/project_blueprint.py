from flask import Blueprint

project = Blueprint('projects', __name__, url_prefix='/projects')


project.route('/', methods=['GET'])
def index():
    return 'hello'
