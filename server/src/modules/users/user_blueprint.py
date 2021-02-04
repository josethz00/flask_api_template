from flask import Blueprint

user_bp = Blueprint('users', __name__, url_prefix='/users')


user_bp.route('/', methods=['GET'])
def index():
    return 'hello'
