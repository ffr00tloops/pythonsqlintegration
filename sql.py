import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
rows = cursor.execute("select * from contacts").fetchall()
print(rows)
connection.commit()