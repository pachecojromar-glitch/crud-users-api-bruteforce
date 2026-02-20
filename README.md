# CRUD Users API + Controlled Brute Force Test

## Project Description

This project is a REST API made with FastAPI.

The API allows you to create, read, update, and delete users (CRUD).

It also includes a simple brute force test against the login endpoint.

The purpose of this project is educational. All tests must be done only in a local environment.

---

## Learning Objectives

- Create a CRUD API.
- Understand how brute force attacks work.
- Measure time and number of attempts.
- Analyze security problems.
- Suggest security improvements.

---

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- SQLite
- Requests

---

## Project Structure

crud-users-api-bruteforce  
│  
├── main.py  
├── brute_force.py  
├── requirements.txt  
└── README.md  

---

## Installation

### 1. Clone the repository

git clone https://github.com/YOUR-USERNAME/crud-users-api-bruteforce.git  
cd crud-users-api-bruteforce  

(Change YOUR-USERNAME to your GitHub username)

---

### 2. Install dependencies

pip install -r requirements.txt  

---

## Run the API

Start the server:

uvicorn main:app --reload  

Open your browser and go to:

http://127.0.0.1:8000/docs  

There you can test all endpoints.

---

## API Endpoints

- POST /users → Create a user
- GET /users → Get all users
- GET /users/{id} → Get one user
- PUT /users/{id} → Update user (not password)
- DELETE /users/{id} → Delete user
- POST /login → Login user

---

## How Login Works

The login checks:

- If the username exists
- If the password is correct

If correct:
Login successful

If wrong:
Login failed

---

## Brute Force Test

The file brute_force.py simulates a simple brute force attack.

It:

- Tries different passwords automatically
- Counts attempts
- Measures total time
- Stops when the correct password is found

To run it:

python brute_force.py  

⚠ The API must be running before you execute the script.

---

## Example Results

- Attempts: 4
- Password found: admin123
- Total time: 0.30 seconds

This shows that weak passwords can be broken quickly.

---

## Security Problems

- Passwords are stored in plain text
- No limit for login attempts
- No account lock
- No extra verification

---

## Security Improvements

To make the system safer, we can add:

- Password hashing (bcrypt)
- Limit login attempts
- Account lock after 5 failed tries
- CAPTCHA
- Two-factor authentication

---

## Ethical Notice

This project is for educational purposes only.

Brute force testing must only be done:

- On your own system
- With permission
- In a local environment

Attacking real systems without permission is illegal.
