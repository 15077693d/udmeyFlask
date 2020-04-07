import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

"""
Create Table
"""
# int -> INTEGER PRIMARY KEY (only need to assign name and pw)
create_user_query = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username text, password text)"
create_student_query = "CREATE TABLE IF NOT EXISTS student (name text PRIMARY KEY, sex text, age integer)"

cursor.execute(create_user_query)
cursor.execute(create_student_query)
# create/ update -> commit
# select -> X commit

connection.commit()
connection.close()
