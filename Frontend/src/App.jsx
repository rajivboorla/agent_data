import { useState, useEffect } from "react";
import API from "./api";
import OAuthSuccess from "./OAuthSuccess";
import Login from "./Login";

function App()  {

  const [agents, setAgents] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const [idFilter, setIdFilter] = useState("");
  const [nameFilter, setNameFilter] = useState("");

  const [sortColumn, setSortColumn] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");

  const url = window.location.pathname;

  if (url === "/oauth-success") {
    return <OAuthSuccess />;
  }

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
      console.error(err);
    }
  };

  const handleLogout = () => {
    localStorage.clear();
    setIsLoggedIn(false);
  };

  // Filtering
  const filteredAgents = agents.filter((agent) =>
    agent.agent_id.toString().includes(idFilter) &&
    agent.name.toLowerCase().includes(nameFilter.toLowerCase())
  );

  // Sorting
  const sortedAgents = [...filteredAgents].sort((a, b) => {

    if (!sortColumn) return 0;

    if (a[sortColumn] < b[sortColumn]) {
      return sortOrder === "asc" ? -1 : 1;
    }

    if (a[sortColumn] > b[sortColumn]) {
      return sortOrder === "asc" ? 1 : -1;
    }

    return 0;

  });

  const handleSort = (column) => {

    if (sortColumn === column) {
      setSortOrder(sortOrder === "asc" ? "desc" : "asc");
    } else {
      setSortColumn(column);
      setSortOrder("asc");
    }

  };

  if (!isLoggedIn) {
    return <Login setIsLoggedIn={setIsLoggedIn} />;
  }

  return (

    <div>

      <h2>Agents</h2>

      <button onClick={fetchAgents}>Get Agents</button>
      <button onClick={handleLogout}>Logout</button>

      <br /><br />

      <table border="1" cellPadding="8">

        <thead>

          <tr>
            <th onClick={() => handleSort("agent_id")} style={{cursor:"pointer"}}>
              Agent ID {sortColumn === "agent_id" ? (sortOrder === "asc" ? "↑" : "↓") : ""}
            </th>

            <th onClick={() => handleSort("name")} style={{cursor:"pointer"}}>
              Name {sortColumn === "name" ? (sortOrder === "asc" ? "↑" : "↓") : ""}
            </th>

            <th>Email</th>
          </tr>

          {/* Filter row */}

          <tr>

            <th>
              <input
                placeholder="Filter ID"
                value={idFilter}
                onChange={(e) => setIdFilter(e.target.value)}
              />
            </th>

            <th>
              <input
                placeholder="Filter Name"
                value={nameFilter}
                onChange={(e) => setNameFilter(e.target.value)}
              />
            </th>

            <th></th>

          </tr>

        </thead>

        <tbody>

          {sortedAgents.map((agent) => (
            <tr key={agent.agent_id}>
              <td>{agent.agent_id}</td>
              <td>{agent.name}</td>
              <td>{agent.email}</td>
            </tr>
          ))}

        </tbody>

      </table>

    </div>

  );
}

export default App;