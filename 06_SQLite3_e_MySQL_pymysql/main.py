# Esse arquivo main, irá conter o código responsável para tratamento de dados
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'
# CRUD = CREATE READ   UPDATE DELETE
# SQL =  INSERT SELECT UPDATE DELETE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: DELETE SEM WHERE DELETA TODOS OS REGISTROS
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
    )
connection.commit()

# Delete mais cuidadoso, coloque sempre WHERE para deletar registros de uma tabela
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name ="{TABLE_NAME}"'
)

# deletar a sequência da tabela
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name ="{TABLE_NAME}"'
    )
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(' 
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
    )
connection.commit()  

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
    )

cursor.execute(sql, {'name':'Qualquer nome', 'weight':'9.9'})
cursor.executemany(sql, (
    {'name':'Alexandre', 'weight':'7.5'},
    {'name':'white', 'weight':'8.5'},
    {'name':'de', 'weight':'9.5'},
    {'name':'mello', 'weight':'6.5'},
    ))
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.close()
    connection.close()