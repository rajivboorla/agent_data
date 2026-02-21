import { useState, useEffect } from "react";
import API from "./api";
import Login from "./Login";

function App() {
  const [agents, setAgents] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check if token exists on load
  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const fetchAgents = async () => {
    try {
      const res = await API.get("/agents");
      setAgents(res.data);
    } catch (err) {
      alert("Error fetching agents");
    }
  };

  const handleLogout = () => {
    localStorage.clear();
    setIsLoggedIn(false);
  };

  if (!isLoggedIn) {
    return <Login setIsLoggedIn={setIsLoggedIn} />;
  }

  return (
    <div>
      <h2>Agents</h2>
      <button onClick={fetchAgents}>Get Agents</button>
      <button onClick={handleLogout}>Logout</button>

      <ul>
        {agents.map((agent) => (
          <li key={agent.agent_id}>
            {agent.name} - {agent.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;