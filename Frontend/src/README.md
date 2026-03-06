main.jsx
   ↓
App.jsx
   ↓
Login.jsx  → calls /Login → stores tokens
   ↓
api.js     → attaches access token
   ↓
/agents    → if 401 → auto refresh → retry


npm audit fix
npm run dev


UI 
-----------------------
|   Welcome Back 👋   |
|  Please login       |
|                     |
|  Username           |
|  Password           |
|  [ Login ]          |
|                     |
| ------ OR --------  |
|  [ Login with Google ]
-----------------------

Backend APIs has below endpoints for accessing it 

POST /auth/login
GET  /auth/google/login
GET  /auth/google/callback