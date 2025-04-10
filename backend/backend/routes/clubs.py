from flask import Blueprint, request, jsonify
from db import get_db_connection
import pymysql

clubs_bp = Blueprint('clubs_bp', __name__)

@clubs_bp.route('/api/clubs', methods=['GET'])
def get_all_clubs():
    try:
        db = get_db_connection()
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM Clubs")
        clubs = cursor.fetchall()

        return jsonify(clubs)
    except Exception as e:
        print("Error fetching clubs:", e)
        return jsonify({'error': 'Failed to fetch clubs'}), 500


@clubs_bp.route('/subscribe', methods=['POST'])
def subscribe_to_club():
    data = request.get_json()
    user_id = data.get('user_id')
    club_id = data.get('club_id')

    if not user_id or not club_id:
        return jsonify({'error': 'Missing user_id or club_id'}), 400

    db = get_db_connection()
    cursor = db.cursor()

    # Check if already subscribed
    check_query = """
        SELECT * FROM User_Clubs WHERE user_id = %s AND club_id = %s
    """
    cursor.execute(check_query, (user_id, club_id))
    existing = cursor.fetchone()

    if existing:
        return jsonify({'message': 'Already subscribed'}), 200

    # Insert new subscription
    insert_query = """
        INSERT INTO User_Clubs (user_id, club_id, role)
        VALUES (%s, %s, 'Member')
    """
    cursor.execute(insert_query, (user_id, club_id))
    db.commit()

    return jsonify({'message': 'Subscribed successfully'}), 201

@clubs_bp.route('/api/reports/club-members', methods=['GET'])
def club_members_report():
    club_id = request.args.get('club_id')  # Get club_id from query parameters
    if not club_id:
        return jsonify({"error": "club_id is required"}), 400  # Return an error if club_id is not provided
    
    print(f"Received club_id: {club_id}")  # Log the club_id to verify

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.user_id, u.username AS user_name, u.email, uc.joined_at
            FROM user_clubs uc
            JOIN users u ON u.user_id = uc.user_id
            WHERE uc.club_id = %s
        """, (club_id,))
        report_data = cursor.fetchall()
        cursor.close()
        conn.close()

        if not report_data:
            print("No members found for this club.")  # Log if no members are found
            return jsonify({"message": "No members found for this club."}), 404

        return jsonify(report_data)

    except Exception as e:
        print(f"Error generating report: {str(e)}")  # Log error to the console
        return jsonify({"error": f"Error generating report: {str(e)}"}), 500
