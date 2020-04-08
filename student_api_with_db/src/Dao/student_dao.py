import sqlite3

from Entity.student import Student


class StudentDao:
    @classmethod
    def find_all(cls):
        connection = sqlite3.connect("data.db")
        query = "SELECT * FROM student"
        result = connection.execute(query)
        students = [Student(*row).__dict__ for row in result]
        connection.close()
        return students

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        query = "SELECT * FROM student WHERE name = ?"
        result = connection.execute(query, (name,))
        row = result.fetchone()
        if row:
            student = Student(*row).__dict__
        else:
            student = None
        connection.close()
        return student

    @classmethod
    def add(cls, student):
        connection = sqlite3.connect("data.db")
        query = "INSERT INTO student VALUES (?,?,?)"
        connection.execute(query, (student.name, student.sex, student.age))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, student):
        connection = sqlite3.connect("data.db")
        query = "UPDATE student SET sex = ?, age = ? WHERE name = ?"
        connection.execute(query, (student.sex, student.age, student.name))
        connection.commit()
        connection.close()

    @classmethod
    def delete(cls,name):
        connection = sqlite3.connect("data.db")
        query = "DELETE FROM student WHERE name = ?"
        connection.execute(query, (name,))
        connection.commit()
        connection.close()

