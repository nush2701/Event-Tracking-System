import mysql.connector
from config import DATABASE_CONFIG

def get_db_connection():
    conn = mysql.connector.connect(
        host = DATABASE_CONFIG['host'],
        user = DATABASE_CONFIG['user'],
        password = DATABASE_CONFIG['password'],
        database = DATABASE_CONFIG['database']
    )
    return conn