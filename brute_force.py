import requests
import time

url = "http://127.0.0.1:8000/login"

username = "admin"

password_list = ["1234", "password", "admin", "admin123", "qwerty"]

start_time = time.time()

attempts = 0

for password in password_list:
    attempts += 1

    response = requests.post(url, json={
        "username": username,
        "password": password,
        "email": "",
        "is_active": True
    })

    print(f"Trying {password} -> {response.json()['message']}")

    if response.json()["message"] == "Login successful":
        print("Password found:", password)
        break

end_time = time.time()

print("Attempts:", attempts)
print("Total time:", end_time - start_time, "seconds")
