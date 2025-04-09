from flask import Blueprint,jsonify,request
from models.event import get_all_events
from db import get_db_connection

events_bp = Blueprint("events",__name__)

@events_bp.route('/api/events',methods=['GET'])
def fetch_all_events():
        events = get_all_events()
        return jsonify(events)

@events_bp.route('/register',methods = ['POST'])
def register_event():
        try:
                data = request.get_json()
                id = data.get('id')
                userId = data.get('userId')

                if not userId or not id:
                        return jsonify({'message':'event id or user id missing'}),400

                conn = get_db_connection()
                cursor = conn.cursor()

                cursor.execute("SELECT user_id FROM Users WHERE user_id = %s", (userId,))
                user_check = cursor.fetchone()
                if not user_check:
                        return jsonify({"message": "Invalid User ID. Please enter a valid user ID."}), 404

                cursor.execute(
                "SELECT * FROM User_Events WHERE user_id = %s AND event_id = %s",
                (userId, id)
                )
                existing = cursor.fetchone()
                if existing:
                        return jsonify({"message": "Already registered for this event."}), 409

                query = """
                INSERT INTO user_events (user_id, event_id)
                VALUES (%s, %s)
                """
                cursor.execute(query, (userId, id))
                conn.commit()

                cursor.close()
                conn.close()

                return jsonify({'message': 'User registered successfully'}), 200

        except Exception as e:
                return jsonify({'message': str(e)}), 500