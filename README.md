# 🚀 FastAPI RBAC Authentication Project

This project is a FastAPI-based backend application implementing:

- ✅ JWT Authentication (Access + Refresh Tokens)
- ✅ Role-Based Access Control (RBAC)
- ✅ Users Management (Admin / Operator roles)
- ✅ Agents Management APIs
- ✅ PostgreSQL Database Integration
- ✅ Secure Password Hashing (bcrypt)
- ✅ Modular Project Structure

---

## 📂 Project Structure
---

## 🔐 Authentication Flow

1. User logs in via `/auth/login`
2. Server validates credentials
3. Server returns:
   - Access Token
   - Refresh Token
4. Access token is required to access protected routes
5. Refresh token generates a new access token
---

## 👥 Roles (RBAC)
Two roles are supported:
- **admin**
  - Full access
  - Can create/update/delete agents
- **operator**
  - Limited access
  - Can view agents

Authorization is handled using dependency injection and role validation in `core/rbac.py`.
---

## 🛡 Security Features

- Passwords are hashed using bcrypt
- JWT tokens include:
  - `sub` (username)
  - `role`
  - `type` (access / refresh)
  - `exp` (expiration)
- Config-driven token expiry via `config.ini`
---
## ⚙️ Configuration
JWT settings are defined in `config.ini`:
---

## 🗄 Database

- SQLAlchemy ORM
- PostgreSQL
- Users table: `practice.t_users_data`
- Agents table: 'practice.t_agents_data'
---

## ▶️ Running the Application

### 1️⃣ Install dependencies

### 2️⃣ Run the server
uvicorn main:app --reload
