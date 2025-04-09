import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/navbar";
import Home from "./pages/Home";
import Clubs from "./pages/Clubs";
import Dashboard from "./pages/Dashboard";
import Notifications from "./pages/Notifications.tsx";

const App = () => {
    return (
        <Router>
            <Navbar />
            <div className="px-6 py-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/clubs" element={<Clubs />} />
          <Route path="/notifications" element={<Notifications />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
