import sqlite3

uId = 1
uPrice = 62300

args = (uId, uPrice)
connection = sqlite3.connect('test.db')

with connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE cars SET price=? WHERE id=?", args)
    print("Number of rows updated: {}".format(cursor.rowcount))


# version 2
uId = 4
connection = sqlite3.connect('test.db')

with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT name, price FROM cars WHERE Id=:Id", {"Id": uId})
    row = cursor.fetchone()
    print(row[0], row[1])
