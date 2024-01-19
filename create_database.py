import datetime
import sqlite3

ts = datetime.datetime.now().strftime("%Y%m%d%H%M")

# define connection and cursor
connection = sqlite3.connect('inspection.db')
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# # create inspection master
command = '''create table if not exists
    material (material_number integer, description text)'''
cursor.execute(command)

# # create inspection transaction
command = '''create table if not exists
    inspection (material text, ts timestamp, prediction float)'''
cursor.execute(command)

# add to master
cursor.execute("insert into material values (1,'mat-1000')")

# get results
cursor.execute("select * from material")
result = cursor.fetchall()
print(result)

# get timestamp
cursor.execute("select datetime('now')")
result = cursor.fetchall()
print(result[0][0])

dt = []
for i in range(10):
    cursor.execute("select datetime('now')")
    result = cursor.fetchall()
    dt.append(result[0][0])

# create test
command = '''create table if not exists
    test (i integer, f float, t text)'''
cursor.execute(command)

# args
sql = "insert into test values (i=?,1,'1')"
arg = int(ts)
arg = 1
cursor.execute(sql, arg)

cursor = connection.execute(sql)


# from datetime import datetime
d = datetime.datetime.strptime(dt[2], "%Y-%m-%d %H:%M:%S")

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
later = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

diff = now - later

# close the cursor and database connection
connection.commit()
cursor.close()
connection.close()

'''
CREATE TABLE `model` (
  `timestamp` integer,
  `filename` text,
  `material` integer,
  `sigma` integer,
  `threshold` float
);

CREATE TABLE `inpsection` (
  `timestamp` integer,
  `material` integer,
  `prediction` float,
  `threshold` float,
  PRIMARY key (timestamp),
  FOREIGN key (material) REFERENCES model(material)
)

'''
