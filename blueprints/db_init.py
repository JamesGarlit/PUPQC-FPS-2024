from blueprints.database.db import Database
from blueprints.database.models import create_table, create_database

def db_start():
    Database()
    # create_database()
    create_table()
        