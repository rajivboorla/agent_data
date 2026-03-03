from database import SessionLocal, engine
from models.user import User
from core.security import hash_password
from database import Base

# Create tables if not exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Dummy users
users = [
    {
        "username": "admin2",
        "email": "admin2@test.com",
        "password": "admin123",
        "role": "admin"
    },
    {
        "username": "operator4",
        "email": "operator4@test.com",
        "password": "operator123",
        "role": "operator"
    },
    {
        "username": "operator3",
        "email": "operator3@test.com",
        "password": "operator123",
        "role": "operator"
    },
    {
        "username": "operator5",
        "email": "operator5@test.com",
        "password": "operator123",
        "role": "operator"  
    },
    {
        "username": "admin3",
        "email": "admin3@test.com",
        "password": "admin123",
        "role": "admin"
    }
]

for user in users:
    existing = db.query(User).filter(User.username == user["username"]).first()
    if not existing:
        new_user = User(
            username=user["username"],
            email=user["email"],
            hashed_password=hash_password(user["password"]),
            role=user["role"]
        )
        db.add(new_user)
        print(f"✅ Created user: {user['username']}")
    else:
        print(f"⚠ User already exists: {user['username']}")

db.commit()
db.close()

print("🎉 Dummy users created successfully")