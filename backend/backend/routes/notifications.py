from flask import Blueprint, request, jsonify
from db import get_db_connection
import pymysql

notifications_bp = Blueprint('notifications_bp', __name__)

@notifications_bp.route('/api/notifications', methods=['GET'])
def get_notifications():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID required'}), 400

    try:
        db = get_db_connection()
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

        cursor.execute("""
            SELECT notification_id, message, created_at
            FROM Notifications
            WHERE user_id = %s
            ORDER BY created_at DESC
        """, (user_id,))
        
        notifications = cursor.fetchall()
        return jsonify(notifications)
    
    except Exception as e:
        print("Error fetching notifications:", e)
        return jsonify({'error': 'Failed to fetch notifications'}), 500
