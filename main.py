from flask import Flask
from blueprints.database.db import Database
from blueprints.database.models import db, user
from blueprints.web.auth import auth_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pup-qc_fps'
db = Database()
user.create_table()


app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)

# user.drop_table()
# print("Table created successfully...")
# Close the database connection
# user.close()