from flask import Blueprint
from ..controller.auth_controller import AuthController
auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(AuthController().login)

auth_bp.route('/register', methods=['POST'])(AuthController().register)

# NOTE: this just for testing jwt, me data can be accessed with request to this endpoint, fe can decode the access_token and get the data
auth_bp.route('/me', methods=['GET'])(AuthController().me)

auth_bp.route('/logout', methods=['GET'])(AuthController().logout)