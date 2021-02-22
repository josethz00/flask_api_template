from flask import Blueprint, request
import json
import hashlib
from werkzeug.exceptions import Unauthorized
from threading import Thread

from .user import User
from src.shared.database.db import db
from src.shared.utils.jwt_handler import JWTHandler
from src.shared.utils.mail_handler import send_email

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('', methods=['GET'])
def index() -> json:
    result = []
    users = db.session.query(User).all()

    for user in users:
        result.append(
            {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        )

    return json.dumps(result), 200


@user_bp.route('', methods=['POST'])
def store() -> json:
    username, email, password, password_confirmation = request.json.values()

    if password != password_confirmation:
        raise Unauthorized('Password and confirmation do not match')

    hashed_password = hashlib.blake2b(bytes(password, 'utf-8')).hexdigest()

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()

    send_email(
        new_user.email,
        f'Welcome {new_user.username}',
        'We are glad to have you here with us, we hope you enjoy our platform'
    )

    return json.dumps({'success': f'Welcome, {new_user.username}!'}), 201


@user_bp.route('/auth', methods=['POST'])
def authenticate() -> json:
    email, password = request.json.values()

    if not email or not password:
        raise Unauthorized('Invalid credentials')

    user = User.query.filter_by(email=email).first()

    if not user:
        raise Unauthorized('Invalid credentials')

    if user.password != hashlib.blake2b(bytes(password, 'utf-8')).hexdigest():
        raise Unauthorized('Invalid credentials')

    jwt_handler = JWTHandler(user.id)

    return json.dumps(
        {
            'id': user.id,
            'username': user.username,
            'token': jwt_handler.sign()
        }
    ), 201
