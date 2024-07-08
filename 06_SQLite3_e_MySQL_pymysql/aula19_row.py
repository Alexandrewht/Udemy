import os
from typing import cast

import dotenv
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
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
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Alexandre', 18)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)
        # print(sql)
        # print(data2)
        # print(result)

    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Fe", "age": 57},
            {"name": "Sa", "age": 35},
            {"name": "Jo", "age": 15},
        )
        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 32),
            ("Cortana", 61),
            ("Alexa", 9)
        )
        result = cursor.executemany(sql, data4)
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    # Lendo dados com SELECT
    with connection.cursor() as cursor:

        # BETWEEN (entre os dois limites)
        small_id = 0
        bigger_id = 100
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )
        cursor.execute(sql, (small_id, bigger_id))
        # print(cursor.mogrify(sql, (small_id, bigger_id)))
        data5 = cursor.fetchall()

        # for row in data5:
        #     print(row)

    # with connection.cursor() as cursor:

    with connection.cursor() as cursor:
        cursor = cast(CURRENT_CURSOR, cursor)

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name=%s, age=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Va', 21, 2))
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()

        print('For 1: ')
        for row in data6:
            print(row)

        
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data7 = (
            {"name": "Ja", "age": 23},
            {"name": "Ta", "age": 52},
            {"name": "Po", "age": 46},
        )
        cursor.executemany(sql, data7)
        
        # Lendo o último ID inserido
        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()

        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)

        # Não retorna o último ID inserido,
        # por usar o cursor.executemany
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', lastIdFromSelect['id'])
        print('rownumber', cursor.rownumber)

    connection.commit()