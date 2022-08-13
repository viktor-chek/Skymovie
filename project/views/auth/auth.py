from flask import request
from project.container import user_service, auth_service
from flask_restx import Namespace, Resource

api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    def post(self):
        data = request.json

        if None in data:
            return "", 400

        user_service.create_user(data)

        return "", 201


@api.route('/login/')
class LoginView(Resource):
    def post(self):
        data = request.json

        if None in data:
            return "", 400

        return auth_service.generate_tokens(data), 201

    def put(self):
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_token(token)

        return tokens, 201
