
from flask import Blueprint
from .auth_route import auth_bp

api = Blueprint('api', __name__)


@api.route('/ping')
def ping():
    return 'pong'


api.register_blueprint(auth_bp, url_prefix='/auth')