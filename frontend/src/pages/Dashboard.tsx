import { useEffect, useState } from "react";

interface Event {
  id: number;
  name: string;
  date: string;
  location: string;
  description: string;
}

function Dashboard() {
  const [events, setEvents] = useState<Event[]>([]);
  const [userId, setUserId] = useState<number | null>(null);

  useEffect(() => {
    const id = prompt("Enter your user ID:");
    if (id) {
      setUserId(parseInt(id));
    }
  }, []);

  useEffect(() => {
    if (userId !== null) {
      fetch(`http://127.0.0.1:5000/api/user-events?user_id=${userId}`)
        .then((res) => res.json())
        .then((data) => {
          const transformed = data.map((event: any) => ({
            id: event.event_id,
            name: event.event_name,
            date: event.event_date,
            location: event.location,
            description: event.description,
          }));
          setEvents(transformed);
        })
        .catch((err) => console.error(err));
    }
  }, [userId]);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">My Registered Events</h1>
      {events.length === 0 ? (
        <p className="text-center text-gray-500">No registered events yet.</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {events.map((event) => (
            <div key={event.id} className="bg-white p-6 rounded-2xl shadow border hover:shadow-lg transition">
              <h2 className="text-xl font-semibold mb-2">{event.name}</h2>
              <p className="text-sm text-gray-600 mb-1">
                <strong>Date:</strong> {new Date(event.date).toLocaleDateString()}
              </p>
              <p className="text-sm text-gray-600 mb-1">
                <strong>Location:</strong> {event.location}
              </p>
              <p className="text-gray-700">{event.description}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Dashboard;