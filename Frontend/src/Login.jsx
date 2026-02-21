import axios from "axios";

function Login({ setIsLoggedIn }) {
  const handleLogin = async () => {
    try {
      const res = await axios.post("http://localhost:8000/login");

      localStorage.setItem("access_token", res.data.access_token);
      localStorage.setItem("refresh_token", res.data.refresh_token);

      setIsLoggedIn(true);
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <div>
      <h2>Login Page</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;