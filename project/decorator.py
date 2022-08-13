from flask import current_app, request, abort
import jwt


def auth_required(func):
    """Декоратор авторизации пользователя"""
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401, "No Authorization")

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, current_app.config['JWT_SECRET'],
                       current_app.config["JWT_ALGORITHM"])
        except Exception:
            abort(401, "JWT Decode Exception")
        return func(*args, **kwargs)

    return wrapper
