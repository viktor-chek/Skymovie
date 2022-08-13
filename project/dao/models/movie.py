from sqlalchemy import Column, String, Integer, Float, ForeignKey
from project.setup.db import models
from sqlalchemy.orm import relationship


class Movie(models.Base):
    __tablename__ = 'movie'

    title = Column(String(300), unique=True, nullable=False)
    description = Column(String(500), unique=True, nullable=False)
    trailer = Column(String(300), unique=True, nullable=False)
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("Director")
