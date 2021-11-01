import sqlite3

connection = sqlite3.connect(database='datab')
cursor = connection.cursor()
cursor.execute('CREATE TABLE students5 (id INTEGER, name TEXT, age INTEGER);')
for i in range(3):
    cursor.execute('INSERT INTO students2 VALUES(' + str(i) + ', "name", "age");')
cursor.execute('SELECT * FROM students2;')
print(cursor.fetchall())

connection.commit()
cursor.close()
connection.close()