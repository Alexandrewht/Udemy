# dados usados da aula 02, para continuar os testes
# PLACEHOLDERS: dados que ficam na hora de registrar os dados
# BINDINGS: dados que ficam na hora de registrar os dados
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
# PLACEHOLDER com BINDINGS (?) 
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
    )

cursor.execute(sql, ['Alexandre', 9.5])
connection.commit()
print(sql)

cursor.close()
connection.close()