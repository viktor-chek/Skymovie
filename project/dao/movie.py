from project.dao.base import BaseDAO
from project.dao.models.movie import Movie


class MoviesDAO(BaseDAO[Movie]):
    """Класс осуществляющий работу с Movie"""
    __model__ = Movie
