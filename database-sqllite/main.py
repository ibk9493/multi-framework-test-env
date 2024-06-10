import sqlite3


with open('query.sql', 'r') as file:
    sql_query = file.read()

conn = sqlite3.connect('sample.db')

cursor = conn.cursor()

cursor.execute(sql_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
