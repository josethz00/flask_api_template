from flask import Blueprint

user = Blueprint('users', __name__, url_prefix='/users')


user.route('/', methods=['GET'])
def index():
    return 'hello'
