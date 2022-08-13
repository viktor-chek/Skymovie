import jwt
from flask import request, current_app, abort
from project.container import user_service

from project.dao.models.user import UserSchema
from project.decorator import auth_required
from flask_restx import Namespace, Resource

api = Namespace('user')
user_schema = UserSchema()


@api.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            user = jwt.decode(jwt=token, key=current_app.config['JWT_SECRET'],
                              algorithms=current_app.config["JWT_ALGORITHM"])
            email = user.get('email')
            return user_schema.dump(user_service.dao.get_user_by_email(email)), 200
        except Exception as e:
            print(f"{e} Не декодирован")
            abort(401)

    @auth_required
    def patch(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            user = jwt.decode(jwt=token, key=current_app.config['JWT_SECRET'],
                              algorithms=current_app.config["JWT_ALGORITHM"])
            user_service.update_user(user['email'], request.json)

            return "", 201

        except Exception as e:
            print(f"{e} Не декодирован")
            abort(401)


@api.route('/password/')
class PassView(Resource):
    @auth_required
    def put(self):
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            user = jwt.decode(jwt=token, key=current_app.config['JWT_SECRET'],
                              algorithms=current_app.config["JWT_ALGORITHM"])
            user_service.update_pass(user['email'], request.json)

            return "", 201

        except Exception as e:
            print(f"{e} Не правильный пароль")
            abort(403)
