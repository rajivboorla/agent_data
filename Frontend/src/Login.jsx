import { useState } from "react";
import "./Login.css";
import { loginUser } from "./api";   // use API file instead of axios
import { FcGoogle } from "react-icons/fc";
function Login({ setIsLoggedIn }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (e) => {

    e.preventDefault();
    setError("");

    if (!username || !password) {
      setError("Please enter username and password");
      return;
    }

    try {

      setLoading(true);

      const response = await loginUser({
        username: username,
        password: password
      });

      // Save tokens
      localStorage.setItem("access_token", response.data.access_token);
      localStorage.setItem("refresh_token", response.data.refresh_token);

      setIsLoggedIn(true);

    } catch (err) {

      if (err.response && err.response.data.detail) {

        setError(err.response.data.detail);
        console.error("Login error:", err.response.data.detail);

      } else {

        setError("Login failed. Please try again.");
        console.error("Login error:", err);

      }

    } finally {

      setLoading(false);

    }
  };

  // Google OAuth Login
  const handleGoogleLogin = () => {
    window.location.href = "http://localhost:8000/auth/google/login";
  };

  return (

    <div className="login-container">

      <div className="login-card">

        <h2>Welcome Back 👋</h2>
        <p>Please login to continue</p>

        <form onSubmit={handleLogin}>

          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          {error && <div className="error-message">{error}</div>}

          <button
            className="login-btn"
            type="submit"
            disabled={loading}
          >
            {loading ? "Logging in..." : "Login"}
          </button>

        </form>

        <div className="divider">OR</div>

        <button className="google-btn" onClick={handleGoogleLogin}>
          <FcGoogle size={20} style={{ marginRight: "8px" }} />
          Login with Google
        </button>

      </div>

    </div>

  );
}

export default Login;