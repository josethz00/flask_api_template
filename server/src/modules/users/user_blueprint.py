from flask import Blueprint, request, jsonify
import json
import hashlib
from werkzeug.exceptions import Unauthorized

from .user import User
from src.shared.database.db import db
from src.shared.utils.jwt_handler import JWTHandler


user_bp = Blueprint('users', __name__, url_prefix='/users')
