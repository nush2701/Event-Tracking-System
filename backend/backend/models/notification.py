import pymysql
from db import get_db_connection

def create_notifications_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Notifications (
        notification_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_notification(user_id, message):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO Notifications (user_id, message)
    VALUES (%s, %s)
    """
    
    cursor.execute(insert_query, (user_id, message))
    connection.commit()
    cursor.close()
    connection.close()

def get_notifications_for_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Notifications WHERE user_id = %s", (user_id,))
    notifications = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return notifications