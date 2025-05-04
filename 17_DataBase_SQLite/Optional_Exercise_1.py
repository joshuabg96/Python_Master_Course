# Create a system to manage the dishes of a menu of a restaurant.
# First create a script called "restaurant.py" and create a function called create_DB() that create a data base with the following two tables:

# CREATE TABLE category(
#                       id INTEGER PRIMARY KEY AUTOINCREMENT,
#                       name VARCHAR(100) UNIQUE NOT NULL)

# CREATE TABLE dish(
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   name VARCHAR(100) UNIQUE NOT NULL,
#                   category_id INTEGER NOT NULL,
#                   FOREIGN KEY(category_id) REFERENCES category(id))
#
# Note: Line FOREIGN KEY(category_id) REferences category(id) indicate an special key(foreign), and it creates a relation between the category of a dish and register of category.

# Call the function and verify that the data base has been created correclty

# Create a function called add_category() that ask the user a name of category and create the category in the data base (Check that if the category exist an error happen because the name is UNIQUE)

# Create an option menu that allows to create a category and exit. Add the following three categories using the option menu
#- First
#- Second
#- Desserts

# Create a function called Add_Dish() that show the categories available and allow them to chosse one, using numbers. It is not necessary to check if the category exist.
# Add the new option to the menu and add the following dishes:
# First: Salad / Tomate Soup
# Second: Fish soup / Chicken and potato
# Desserts: Flan / Fruit

# Create a function called menu() that show all the dishes with the dishes sorted by category


import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"restaurant.db")

connection = sqlite3.connect(file_path)
cursor = connection.cursor()

def Create_DB():
    try:
        cursor.execute('''CREATE TABLE category( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("Category table exist")
    else:
        print("Category table has been created correctly")

    try:
        cursor.execute('''CREATE TABLE dish(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(100) UNIQUE NOT NULL,
                        category_id INTEGER NOT NULL,
                        FOREIGN KEY(category_id) REFERENCES category(id))''')
    except:
        print("Dish Table exist")
    else:
        print("Dish table has been created correctly")
    connection.commit()
    connection.close()


def Add_Category():
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()
    category = input("Give me the name of the category\n")
    try:
        cursor.execute("INSERT INTO category VALUES (null,'{}')".format(category))
    except sqlite3.IntegrityError:
        print("The Category {} already exist".format(category))
    else:
        print("The category {} has been created correctly".format(category))

    connection.commit()
    connection.close()

def Add_Dish():
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    print("Choose a category to add a dish")
    categories = cursor.execute("SELECT * FROM category").fetchall()
    for cat in categories:
        print("{} {}".format(cat[0], cat[1]))
    choose = int(input("\n"))
    dish = input("Name of the new Dish: ")
    try:
        cursor.execute("INSERT INTO dish VALUES (null, '{}',{})".format(dish, choose))
    except sqlite3.IntegrityError:
        print("The Dish {} already exist".format(dish))
    else:
        print("The Dish {} has been added correctly to category {}". format(dish, str(choose)))
    
    connection.commit()
    connection.close()


def Menu():
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    categories = cursor.execute("SELECT * FROM category").fetchall()
    for cat in categories:
        print(cat[1])
        dishes = cursor.execute("SELECT * FROM dish WHERE category_id={}".format(cat[0])).fetchall()
        for dish in dishes:
            print("\t" + dish[1])
    connection.commit()
    connection.close()



# Menu Options
while True:
    print("Welcome to restaurant system\n")
    option = input("Introduce one option:\n[1] Add category\n[2]Add Dish\n[3]Show Menu\n[4]Exit\n")
    match int(option):
        case 1:
            Add_Category()
        case 4:
            break
        case 2:
            Add_Dish()
        case 3:
            Menu()
        case _:
            print("Incorrect Option, choose another one")
