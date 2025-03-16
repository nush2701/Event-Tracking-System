from db import get_db_connection

def create_user_clubs_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS User_Clubs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        club_id INT NOT NULL,
        role ENUM('Admin', 'Member') DEFAULT 'Member',
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status ENUM('Active', 'Inactive', 'Banned') DEFAULT 'Active',
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (club_id) REFERENCES clubs(club_id) ON DELETE CASCADE
    )
    """
    
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def add_user_to_club(user_id, club_id, role='Member'):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO User_Clubs (user_id, club_id, role) 
    VALUES (%s, %s, %s)
    """
    
    cursor.execute(insert_query, (user_id, club_id, role))
    connection.commit()
    cursor.close()
    connection.close()

def get_user_clubs(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    select_query = "SELECT * FROM User_Clubs WHERE user_id = %s"
    cursor.execute(select_query, (user_id,))
    
    clubs = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return clubs
