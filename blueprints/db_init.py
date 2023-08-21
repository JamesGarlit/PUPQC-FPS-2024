from blueprints.database.db import Database
from blueprints.database.models import User

def db_start():
    Database()
    User()
