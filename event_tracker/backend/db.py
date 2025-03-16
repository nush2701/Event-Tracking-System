import pymysql
from config import DATABASE_CONFIG

def get_db_connection():
    conn = pymysql.connect(
        host = DATABASE_CONFIG['host'],
        user = DATABASE_CONFIG['user'],
        password = DATABASE_CONFIG['password'],
        database = DATABASE_CONFIG['database']
    )
    return conn

def execute_query():
    query = input("Enter the query: ")
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return "Query executed successfully!"