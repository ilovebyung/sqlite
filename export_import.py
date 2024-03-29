import sqlite3
from sqlite3.dbapi2 import connect

cars = (
    (1, 'Audi', 52643),
    (2, 'Mercedes', 57642),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


def writeData(data):
    f = open('cars.sql', 'w')
    with f:
        f.write(data)


connect = sqlite3.connect(':memory:')

with connect:
    cur = connect.cursor()
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
    cur.execute("DELETE FROM cars WHERE price < 30000")
    data = '\n'.join(connect.iterdump())
    writeData(data)
