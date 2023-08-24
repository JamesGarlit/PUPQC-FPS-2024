from .bp_init import blueprint_start
from .db_init import db_start

def initialize():
    app = blueprint_start()
    db_start()

    return app

