from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.dao.models.director import Director


class DirectorService:
    """Сервис режиссеров"""
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        """Получение по pk"""
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        """Получение всех режиссеров"""
        return self.dao.get_all(page=page)
