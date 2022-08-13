from project.dao import GenresDAO
from project.dao.director import DirectorDAO
from project.dao.movie import MoviesDAO
from project.dao.user import UserDAO

from project.services.genres_service import GenresService
from project.services.directors_service import DirectorService
from project.services.movies_service import MovieService
from project.services.users_service import UserService
from project.services.auth_service import AuthService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
