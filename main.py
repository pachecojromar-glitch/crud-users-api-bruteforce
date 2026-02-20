from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI(title="CRUD Users API")

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    email TEXT,
    is_active BOOLEAN
)
""")
conn.commit()

class User(BaseModel):
    username: str
    password: str
    email: str = None
    is_active: bool = True


@app.post("/users")
def create_user(user: User):
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email, is_active) VALUES (?, ?, ?, ?)",
            (user.username, user.password, user.email, user.is_active)
        )
        conn.commit()
        return {"message": "User created"}
    except:
        raise HTTPException(status_code=400, detail="Username already exists")


@app.get("/users")
def get_users():
    cursor.execute("SELECT id, username, email, is_active FROM users")
    return cursor.fetchall()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    cursor.execute("SELECT id, username, email, is_active FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    cursor.execute(
        "UPDATE users SET username=?, email=?, is_active=? WHERE id=?",
        (user.username, user.email, user.is_active, user_id)
    )
    conn.commit()
    return {"message": "User updated"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    return {"message": "User deleted"}


@app.post("/login")
def login(user: User):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (user.username, user.password)
    )
    result = cursor.fetchone()

    if result:
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}
