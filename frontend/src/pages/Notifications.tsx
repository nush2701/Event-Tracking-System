import { useEffect, useState } from "react";

interface Notification {
  notification_id: number;
  message: string;
  created_at: string;
}

const Notifications = () => {
  const [userId, setUserId] = useState<number | null>(null);
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    const id = prompt("Enter your user ID to see notifications:");
    if (id) setUserId(parseInt(id));
  }, []);

  useEffect(() => {
    if (userId !== null) {
      fetch(`http://localhost:5000/api/notifications?user_id=${userId}`)
        .then((res) => res.json())
        .then((data) => setNotifications(data))
        .catch((err) => console.error(err));
    }
  }, [userId]);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-2xl font-bold mb-4 text-center">Notifications</h1>
      {notifications.length === 0 ? (
        <p className="text-center text-gray-500">No notifications.</p>
      ) : (
        <div className="space-y-4">
          {notifications.map((note) => (
            <div key={note.notification_id} className="bg-white p-4 shadow rounded-xl border">
              <p>{note.message}</p>
              <p className="text-xs text-gray-400 mt-2">{new Date(note.created_at).toLocaleString()}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Notifications;