# fazendo consultas 
# SELECT
import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

print('-'*20)
print('SELECT ALL FROM TABLE')
print('-'*20)

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
    )

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print('-'*20)
print('SELECT ID 3')
print('-'*20)

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
    )

row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()