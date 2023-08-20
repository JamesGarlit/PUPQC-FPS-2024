from .db import Database

# instance of the Database class
db = Database()

class User:
    def create_db(self):
        query = """
            IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'your_database_name') THEN
                CREATE DATABASE your_database_name;
            END IF;
        """
        db.cursor.execute(query)
        db.conn.commit()
        
    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                fullname varchar(100) NOT NULL,
                username varchar(50) NOT NULL,
                password varchar(255) NOT NULL,
                email varchar(50) NOT NULL UNIQUE
            )
        """
        db.cursor.execute(query)
        db.conn.commit()
        
    def drop_table(self):
        query = "DROP TABLE IF EXISTS users"
        db.cursor.execute(query)
        db.conn.commit()

# instance of the User class
user = User()
