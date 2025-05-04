import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"Connection.db")

connection = sqlite3.connect(file_path)

cursor = connection.cursor()

#cursor.execute("CREATE TABLE users (Name VARCHAR(100), Age INTEGER, email VARCHAR(100))")

#cursor.execute("INSERT INTO users VALUES ('Hector',27,'Hector@example.com')")

#cursor.execute("SELECT * FROM users ")
#users = cursor.fetchone()
#print(users)

users = [
    ('Mario',51,'mario@example.com'),
    ('Mercedes',38,'mercedes@example.com'),
    ('Juan',19,'juan@example.com'),
]

#cursor.executemany("INSERT INTO users VALUES (?,?,?)", users)

cursor.execute("SELECT * FROM users")

users_Get = cursor.fetchall()
for user in users_Get:
    print(user)


connection.commit()

connection.close()