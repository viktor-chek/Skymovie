from marshmallow import Schema, fields
from sqlalchemy import Column, String
from project.setup.db import models


class User(models.Base):
    __tablename__ = 'user'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    name = Column(String(50))
    surname = Column(String(100))
    favorite_genre = Column(String(100))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Int()
