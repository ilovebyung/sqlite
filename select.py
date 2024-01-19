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
with connection:
    cursor = connection.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    result = cursor.fetchall()[0][0]
    print(f'result: {result}')
