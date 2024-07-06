# Dados puxados da aula 07
# UPDATE

# Esse arquivo main, irá conter o código responsável para tratamento de dados
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

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
    # DELETE
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "1"'
    )
    connection.commit()

    # UPDATE
    # CUIDADO COM O UPDATE PARA SOBRESCREVE TODOS OS REGISTROS SEM WHERE,
    # Então use o WHERE para sobrescrever apenas o registro selecionado.
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="OUTRO NOME QUALQUER", weight=67.89 '
        'WHERE id = "4"'
    )
    connection.commit()

    
    cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
    )
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()