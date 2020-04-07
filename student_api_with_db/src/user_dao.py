import sqlite3

from user import User


class UserDao:
    @classmethod
    def find_all(cls):
        connection = sqlite3.connect("data.db")
        query = "SELECT * FROM user"
        result = connection.execute(query)
        users = [User(*row) for row in result]
        connection.close()
        return users

    @classmethod
    def add(cls, username, password):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO user (username, password) VALUES (?, ?)"
        cursor.execute(query, (username, password))
        connection.commit()
        connection.close()

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM user WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            # * row -> row[0], row[1], row[2]
            user = User(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM user WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            # * row -> row[0], row[1], row[2]
            user = User(*row)
        else:
            user = None
        connection.close()
        return user
