import { useEffect } from "react";

function OAuthSuccess() {

  useEffect(() => {

    const params = new URLSearchParams(window.location.search);

    const access = params.get("access_token");
    const refresh = params.get("refresh_token");

    if (access) {
      localStorage.setItem("access_token", access);
      localStorage.setItem("refresh_token", refresh);

      window.location.href = "/";
    }

  }, []);

  return <h2>Logging you in with Google...</h2>;
}

export default OAuthSuccess;