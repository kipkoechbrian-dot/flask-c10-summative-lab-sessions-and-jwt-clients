from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from config import db
from models import User
from schemas import user_schema


class Signup(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"error": "Username and password are required."}, 400

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return {"error": "Username already exists."}, 400

        user = User(username=username)
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=user.id)

        return {
            "user": user_schema.dump(user),
            "access_token": access_token
        }, 201


class Login(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if not user:
            return {"error": "Invalid username or password."}, 401

        if not user.authenticate(password):
            return {"error": "Invalid username or password."}, 401

        access_token = create_access_token(identity=user.id)

        return {
            "user": user_schema.dump(user),
            "access_token": access_token
        }, 200


class Me(Resource):

    @jwt_required()
    def get(self):

        current_user_id = get_jwt_identity()

        user = User.query.get(current_user_id)

        if not user:
            return {"error": "User not found."}, 404

        return user_schema.dump(user), 200