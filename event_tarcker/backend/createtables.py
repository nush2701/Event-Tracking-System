import pymysql
from db import get_db_connection

def create_table():
    query = input("Enter the query: ")
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return "Query executed successfully!"