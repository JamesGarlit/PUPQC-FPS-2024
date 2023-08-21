from blueprints.database.db import Database
from blueprints.database.models import user

def db_start():
    Database()
    user.create_table()
