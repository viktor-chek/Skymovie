from project.dao.base import BaseDAO
from project.dao.models.director import Director


class DirectorDAO(BaseDAO[Director]):
    """Класс осуществляющий работу с Director"""
    __model__ = Director
