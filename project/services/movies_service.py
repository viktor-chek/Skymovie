from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.models.movie import Movie


class MovieService:
    """Сервис фильмов"""
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        """Получение по pk"""
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> list[Movie]:
        """Получение всех режиссеров"""
        return self.dao.get_all(page=page, status=status)
