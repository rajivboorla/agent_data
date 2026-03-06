import { useState, useEffect } from "react";
import API from "./api";
import OAuthSuccess from "./OAuthSuccess";
import Login from "./Login";

function App() {

  const [agents, setAgents] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const url = window.location.pathname;

  // ✅ Handle OAuth redirect
  if (url === "/oauth-success") {
    return <OAuthSuccess />;
  }

  // Check if token exists on load
  useEffect(() => {
    console.log("Checking for existing token...", localStorage.getItem("access_token"));
    const token = localStorage.getItem("access_token");

    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const fetchAgents = async () => {
    try {

      const res = await API.get("/agents", {
        params: {
          sort_by: "name",
          order: "asc",
        },
      });

      setAgents(res.data);
      console.log("Agents fetched:", res.data);

    } catch (err) {

      alert("Error fetching agents");
      console.error("Error fetching agents:", err);

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