// src/api.js
import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

// Attach access token automatically
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

// Handle 401 → Refresh Token
API.interceptors.response.use(
  (response) => response,

  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem("refresh_token");

        const res = await axios.post(
          "http://localhost:8000/refresh",
          { refresh_token: refreshToken }
        );

        const newAccessToken = res.data.access_token;

        localStorage.setItem("access_token", newAccessToken);

        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

        return API(originalRequest);

      } catch (err) {

        console.log("Refresh failed. Please login again.");

        localStorage.clear();
        window.location.href = "/";
      }
    }

    return Promise.reject(error);
  }
);


// ----------------------------
// AUTH APIs
// ----------------------------

// Regular login
export const loginUser = (data) => {
  return API.post("/users/login", data);
};

// Google OAuth login
export const googleLogin = (token) => {
  return API.post("/oauth/google", {
    token: token
  });
};

// Example protected API
export const getAgents = () => {
  return API.get("/agents");
};

export default API;