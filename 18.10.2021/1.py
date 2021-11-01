import sqlite3

connection = sqlite3.connect('db')
cursor = connection.cursor()
cursor.execute('SELECT COUNT(*) FROM level_1')
cursor.execute('SELECT question, answer1, answer2, answer3, answer4 FROM level_1 WHERE id=1')
print(cursor.fetchall())
connection.commit()

cursor.close()
connection.close()