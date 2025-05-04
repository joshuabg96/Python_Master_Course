import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"products.db")

connection = sqlite3.connect(file_path)
cursor = connection.cursor()

cursor.execute("SELECT * FROM users WHERE age=27")
user = cursor.fetchone()
print(user)
user = cursor.fetchone()
print(user)

cursor.execute("UPDATE users SET name='Hector Costa', age=30 WHERE dni=1111")

cursor.execute("Delete FROM users WHERE dni=1111")

connection.commit()
connection.close()