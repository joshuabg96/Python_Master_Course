import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
#file_path = os.path.join(script_dir,"Keys.db")
file_path = os.path.join(script_dir,"products.db")

connection = sqlite3.connect(file_path)
cursor = connection.cursor()

users = [
    ('1111','Hector', 27, 'hector@example.com'),
    ('2222','Mario',51,'mario@example.com'),
    ('3333','Mercedes',38,'mercedes@example.com'),
    ('4444','Juan',19,'juan@example.com'),
]

# Primary Key: Identifier of every register
#cursor.execute('''CREATE TABLE users(
#               dni VARCHAR(9) PRIMARY KEY,
#               name VARCHAR(100),
#               age INTEGER,
#               email VARCHAR(100))''')

#cursor.execute('''CREATE TABLE products(
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               name VARCHAR(100),
#               brand INTEGER,
#               price FLOAT NOT NULL)''')

#cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)

products = [
    ("Keyboard", "Logitech", 19.95),
    ("Monitor", "LG", 89.95)
]

#cursor.executemany("INSERT INTO products VALUES (null,?,?,?)", products)

cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
for product in products:
    print(product)

#cursor.execute(''' 
#                CREATE TABLE users (
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               dni VARCHAR(9) UNIQUE,
#               name VARCHAR(100),
#               age INTEGER,
#               email VARCHAR (100))''')

#cursor.executemany("INSERT INTO users VALUES (null,?,?,?,?)", users)

connection.commit()
connection.close()