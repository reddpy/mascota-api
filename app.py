from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from resources import register_resources
from config import Config 
from models import register_models
from flask_jwt import JWT

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
register_models()
register_resources(api)

from utils.login import authenticate, identity
jwt = JWT(app, authenticate, identity)