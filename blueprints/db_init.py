from blueprints.database.db import Database
from blueprints.database.models import create_table

def db_start():
    Database()
    create_table()
