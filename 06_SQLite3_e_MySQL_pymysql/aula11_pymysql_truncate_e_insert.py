import pymysql
import dotenv
import os

dotenv.load_dotenv()
TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # TRUNCATE LIMPA A TABELA
    connection.commit()

    # Começo a manipular dados a partir daqui
    with connection.cursor() as cursor:
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("Alexandre", 20) '
        )
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("White", 15) '
        )
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES ("Mello", 10) '
        )
    connection.commit()