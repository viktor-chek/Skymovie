import os
import sys
from project.setup.db import db
from project.config import DevelopmentConfig
from project.dao.models import director, genre, movie, user
from project.server import create_app

path = os.path.abspath('.')
sys.path.insert(1, path)


app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
