import sqlite3


class Database:

    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user (user_id INTEGER PRIMARY KEY)")
        self.connection.commit()

    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        self.connection.commit()

    def get_all_users(self):
        users = self.cursor.execute('SELECT * FROM users').fetchall()
        return users