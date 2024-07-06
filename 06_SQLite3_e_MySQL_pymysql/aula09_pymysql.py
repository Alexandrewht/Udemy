from dotenv import load_dotenv
import os

load_dotenv('config.env')

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

print(f"Username: {db_username}, Password: {db_password}")