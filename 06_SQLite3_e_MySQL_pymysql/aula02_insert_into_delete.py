# dados usados da aula 01, para continuar os testes
# INSERT INTO, DELETE
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
connection.commit()  # Salva as alterações

# Registrar valores nas colunas da tabela
# CUIDADO: Se estiver recebendo valores do usuário, pode receber SQL INJECTION.
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES '
    '(NULL, "Alexandre white", 9.9), (NULL, "Alexandre black", 9.8)'
    )
connection.commit()

cursor.close()
connection.close()