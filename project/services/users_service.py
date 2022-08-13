import base64
import hashlib
import hmac

from flask import current_app, abort
from project.dao.user import UserDAO


class UserService:
    """Сервис для работы с пользователем"""
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_email(self, email):
        """Запрос юзера по email"""
        return self.dao.get_user_by_email(email)

    def create_user(self, data):
        """Создание пользователя"""
        data["password"] = self.generate_password(data["password"])

        return self.dao.create_user(data)

    def generate_password(self, password):
        """Функция кодирования пароля в hash"""
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt=current_app.config["PWD_HASH_SALT"],
            iterations=current_app.config["PWD_HASH_ITERATIONS"]
        )
        return base64.b64encode(hash_digest)

    def update_user(self, user, data):
        """Обновление данных пользователя"""
        return self.dao.user_update(user, data)

    def update_pass(self, user_mail, pass_date):
        """Обновление пароля пользователя"""
        user = self.get_by_email(user_mail)

        if self.compare_passwords(user.password, pass_date["old_password"]):
            hash_new_pass = self.generate_password(pass_date["new_password"])
            return self.dao.update_pass(user.email, hash_new_pass)

        else:
            abort(403)

    def compare_passwords(self, hash_password, password):
        """Функция сверки hash паролей"""
        decoded_digest = base64.b64decode(hash_password)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt=current_app.config["PWD_HASH_SALT"],
            iterations=current_app.config["PWD_HASH_ITERATIONS"]
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
