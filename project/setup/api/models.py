from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Жанр'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Имя режиссера'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название фильма'),
    'description': fields.String(required=True, max_length=600, example='Описание картины'),
    'trailer': fields.String(required=True, max_length=300, example='ссылка на трейлер'),
    'year': fields.Integer(required=True, example='Год выпуска картины'),
    'rating': fields.Float(required=True, example='Рейтинг картины'),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=200, example='netflix@yandex.ru'),
    'password': fields.String(required=True, max_length=100, example='Пароль228')
})
