import datetime
import calendar
import jwt
from flask import current_app, abort


from project.services.users_service import UserService


class AuthService:
    """Сервис авторизации"""
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, data, is_refresh=False):
        """Функция генерации JWT"""
        user = self.user_service.get_by_email(data['email'])
        if not user:
            abort(404)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, data['password']):
                abort(400)

        data = {
            "email": user.email
        }

        # 30 min for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, current_app.config['JWT_SECRET'],
                                  algorithm=current_app.config['JWT_ALGORITHM'])

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, current_app.config['JWT_SECRET'],
                                   algorithm=current_app.config['JWT_ALGORITHM'])
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_token(self, refresh_token):
        """Обновления токена"""
        data = jwt.decode(jwt=refresh_token, key=current_app.config['JWT_SECRET'],
                          algorithms=current_app.config["JWT_ALGORITHM"])

        return self.generate_tokens(data, is_refresh=True)
