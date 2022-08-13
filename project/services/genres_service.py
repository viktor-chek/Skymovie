from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.models.genre import Genre


class GenresService:
    """Сервис жанров"""
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        """Получение по pk"""
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        """Получение всех режиссеров"""
        return self.dao.get_all(page=page)
