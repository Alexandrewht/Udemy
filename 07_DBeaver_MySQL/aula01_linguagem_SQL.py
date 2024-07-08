# https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/
import pymysql
import dotenv
import os

dotenv.load_dotenv()

# vamos continuar com a mesma porta 3306
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

print(os.environ['MYSQL_HOST'])

with connection:
    with connection.cursor() as cursor:
        print(cursor)