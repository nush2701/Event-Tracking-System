import { useEffect, useState } from "react";

interface Event {
  id: number;
  name: string;
  date: string;
  location: string;
  description: string;
}

const handleRegister = async (id: number) => {
  const userId = prompt("Enter your user id: ");

  if (!userId) {
    alert("USER ID is required.");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userId: parseInt(userId), id: id }),
    });

    if (response.ok) {
      alert("Successfully Registered!");
    } else {
      const data = await response.json();
      alert(`Failed Registration: ${data.message}`);
    }
  } catch (err) {
    console.error("Error during registration: ", err);
    alert("Something went wrong");
  }
};

function Home() {
  const [events, setEvents] = useState<Event[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/events")
      .then((res) => res.json())
      .then((data) => setEvents(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-8">Upcoming University Events</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {events.map(event => (
          <div
            key={event.id}
            className="bg-white p-6 rounded-2xl shadow-md border hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold mb-2">{event.name}</h2>
            <p className="text-sm text-gray-600 mb-1"><strong>Date:</strong> {event.date}</p>
            <p className="text-sm text-gray-600 mb-1"><strong>Location:</strong> {event.location}</p>
            <p className="text-gray-700 mb-4">{event.description}</p>
            <button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700" onClick={() => handleRegister(event.id)}>
              Register
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
