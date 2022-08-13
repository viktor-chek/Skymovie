from project.dao.base import BaseDAO
from project.dao.models.genre import Genre


class GenresDAO(BaseDAO[Genre]):
    """Класс осуществляющий работу с Genre"""
    __model__ = Genre
