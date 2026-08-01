from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key-change-this"