import React from "react";
import { Link } from "react-router-dom";

const Navbar: React.FC = () => {
  return (
    <nav className="bg-white shadow-md py-4 px-6 flex justify-between items-center">
      <h1 className="text-2xl font-bold text-blue-600">Event Tracker</h1>
      <div className="space-x-6">
        <Link to="/" className="text-gray-700 hover:text-blue-500 font-medium">
          Home
        </Link>
        <Link to="/dashboard" className="text-gray-700 hover:text-blue-500 font-medium">
          Dashboard
        </Link>
        <Link to="/clubs" className="text-gray-700 hover:text-blue-500 font-medium">
          Clubs
        </Link>
        <Link to="/notifications" className="text-gray-700 hover:text-blue-500 font-medium">
          Notifications
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;