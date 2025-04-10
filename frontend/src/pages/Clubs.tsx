import { useEffect, useState } from "react";

interface Club {
  id: number;
  name: string;
  description: string;
}

const Clubs = () => {
  const [clubs, setClubs] = useState<Club[]>([]);
  const [reportData, setReportData] = useState<any[]>([]);
  const [showReport, setShowReport] = useState<boolean>(false);

  useEffect(() => {
    fetch("http://localhost:5000/api/clubs")
      .then((res) => res.json())
      .then((data) => {
        const transformed = data.map((club: any) => ({
          id: club.club_id,
          name: club.club_name,
          description: club.description,
        }));
        setClubs(transformed);
      })
      .catch((err) => console.error("Error fetching clubs:", err));
  }, []);

  const subscribeToClub = async (clubId: number) => {
    const userId = prompt("Enter your user ID to subscribe:");
    if (!userId) return alert("User ID is required!");

    try {
      const res = await fetch("http://localhost:5000/subscribe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: parseInt(userId), club_id: clubId }),
      });

      const data = await res.json();
      alert(data.message);
    } catch (err) {
      console.error(err);
      alert("Something went wrong.");
    }
  };

  // Function to generate the club members report
  const generateReport = async (clubId: number) => {
    try {
      const res = await fetch(`http://127.0.0.1:5000/api/reports/club-members?club_id=${clubId}`);
      const data = await res.json();
      
      console.log("Received Data:", data); // Log to check if data is correct
  
      if (res.ok) {
        setReportData(data);  // Update the state with report data
        setShowReport(true);   // Set the flag to display the report
      } else {
        alert(data.message || "Failed to generate report");
      }
    } catch (err) {
      console.error("Failed to generate report:", err);
      alert("Error generating report");
    }
  };  

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">University Clubs</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {clubs.map((club) => (
          <div
            key={club.id}
            className="bg-white p-6 rounded-2xl shadow border hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold mb-2">{club.name}</h2>
            <p className="text-gray-700 mb-4">{club.description}</p>
            <div className="space-y-2">
              {/* Button for subscribing */}
              <button
                onClick={() => subscribeToClub(club.id)}
                className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 w-full"
              >
                Subscribe
              </button>

              {/* Button for generating the club report */}
              <button
                onClick={() => generateReport(club.id)}
                className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 w-full"
              >
                Generate Club Report
              </button>
            </div>
          </div>
        ))}
      </div>

      {showReport && reportData.length > 0 ? (
  <div className="mt-8 bg-white p-6 rounded-2xl shadow">
    <h3 className="text-xl font-semibold mb-4">Club Members Report</h3>
    <table className="min-w-full bg-white border border-gray-200">
      <thead>
        <tr className="bg-gray-100 border-b">
          <th className="py-2 px-4 text-left">User ID</th>
          <th className="py-2 px-4 text-left">Name</th>
          <th className="py-2 px-4 text-left">Email</th>
          <th className="py-2 px-4 text-left">Joined At</th>
        </tr>
      </thead>
      <tbody>
        {reportData.map((user: any) => (
          <tr key={user.user_id} className="border-b">
            <td className="py-2 px-4">{user.user_id}</td>
            <td className="py-2 px-4">{user.user_name}</td>
            <td className="py-2 px-4">{user.email}</td>
            <td className="py-2 px-4">{new Date(user.joined_at).toLocaleDateString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
) : (
  showReport && <div>No members found or failed to fetch data.</div>
)}
    </div>
  );
};

export default Clubs;