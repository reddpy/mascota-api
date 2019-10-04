import os
import flask_jwt
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    flask_jwt.CONFIG_DEFAULTS['JWT_AUTH_USERNAME_KEY'] = 'email'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY='super-secret-test'

    PET_FINDER_API_KEY = "J3MWqYzmScOvw1Pl5FwH9Bj5yQ6q59tjhGfgkv29zEJqEsPsVx"
    PET_FINDER_CLIENT_KEY = "OlIkuCz4rpS4Gh92wKVNJG4W3F1q1w5AsfiajTSQ"