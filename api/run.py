import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from . import models, resources

app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
