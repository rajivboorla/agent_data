
---- This removes it only from Git, not from your system.
git rm --cached .gitignore

| Task                                 | Command                                                     |
| ------------------------------------ | ----------------------------------------------------------- |
| Remove project `.gitignore` from Git | `git rm --cached .gitignore`                                |
| Use global ignore instead            | `git config --global core.excludesfile ~/.gitignore_global` |

removes file from tracking --> git rm --cached .gitignore
commit the removal --> git commit -m "Remove .gitignore from repository"
push the changes to repo -- > git push


<!-- It starts a local development server, which usually runs on:
http://127.0.0.1:8000
or
http://localhost:8000

so http is allowed here

Reasons HTTP is okay here:
Only your machine is accessing it
No internet exposure
Used only for development and testing


3️⃣ What happens in Production

In production we normally add a reverse proxy like:

Nginx

Apache HTTP Server

Then we install an SSL certificate (often from Let's Encrypt).

Then the API becomes:

https://api.company.com/agents

Flow:

Client
   ↓ HTTPS
Nginx (SSL termination)
   ↓ HTTP
FastAPI App

Browser / React App
        ↓
     HTTPS
        ↓
     Nginx
        ↓
     FastAPI (Uvicorn)
        ↓
     Database

5️⃣ Why developers don't use HTTPS locally
Because it requires:
SSL certificates
Extra configuration
Browser trust setup

So during development HTTP is used for simplicity     

Client → HTTPS → Nginx
Nginx → HTTP → FastAPI
 -->