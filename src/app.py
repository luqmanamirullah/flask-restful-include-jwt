# base starting point for the flask application

from flask import Flask
from .route import api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.config['DEBUG'] = True

app.url_map_class.strict_slashes = False # allows for trailing slashes on routes
app.register_blueprint(api, url_prefix='/api')