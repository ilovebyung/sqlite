import datetime
import sqlite3
import sys

try:
    # define connection and cursor
    # connection = sqlite3.connect('inspection.db')
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    # # create inspection master
    sql = '''create table if not exists
        material (material_number integer, description text)'''
    # sql = "DROP TABLE IF EXISTS cars"
    cursor.execute(sql)

    # # create inspection transaction
    # cursor.execute(command)
    cursor.execute('SELECT SQLITE_VERSION()')
    result = cursor.fetchall()[0]
    print(result)
except sqlite3.Error as e:
    print(f'an error has occured: {e}')
    sys.exit(1)
finally:
    connection.close()

# version 2
connection = sqlite3.connect('test.db')
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

with connection:

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS cars")
    cursor.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cursor.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
