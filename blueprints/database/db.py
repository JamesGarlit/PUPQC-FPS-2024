import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            database='sampledb',
            user='postgres',
            password='1234',
            host='127.0.0.1',
            port='5432'
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        
# instance of the Database class
db = Database()
