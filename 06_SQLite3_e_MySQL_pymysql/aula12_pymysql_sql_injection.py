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
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES (%s, %s) '  # %s são os valores que serão inseridos depois
        )
        data = ('Alexandre', 30)
        result = cursor.execute(sql, data)


        # Parte do código sem proteção
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
        print(sql, data)
        print(result)

    # CUIDADO COM SQL INJECTION, por exemplo
    # "'); DROP TABLE customers; --"
    # Irá tentar dropar a tabela, simbolos padrões do MySQL.
    with connection.cursor() as cursor:
        try:
            malicious_input = '"); DROP TABLE customers; --'
            sql_injection = (
                f'INSERT INTO {TABLE_NAME} '
                f'(name, age) VALUES ("{malicious_input}", 10)'
            )
            cursor.execute(sql_injection)
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"SQL Injection falhou: {e}")
    with connection.cursor() as cursor:
        try:
            cursor.execute(f'SELECT * FROM {TABLE_NAME}')
            result = cursor.fetchall()
            for row in result:
                print(row)
        except pymysql.MySQLError as e:
            print(f"Tabela {TABLE_NAME} não encontrada: {e}")
    connection.commit()