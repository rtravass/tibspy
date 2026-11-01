# class Customer: 
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def display_info(self):
#         print(self.name)
#         print(self.email)

# customer1 = Customer("Ryan","abc@gmail.com")
# customer2 = Customer("Oli","xyz@gmail.com")
# customer1.display_info()
# customer2.display_info()

#=============================Inheritance======================================

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def login(self):
#         print(f"{self.name} logged in")

# class DataEngineer(Employee):
#     def build_pipeline(self):
#         print(f"{self.name} is building a pipeline")

# engineer = DataEngineer("Jo")
# engineer.login()
# engineer.build_pipeline()


#=================================super() to reuse parent logic ===============

# class Employee:
#     def __init__(self, name):
#         self.name = name

# class DataEngineer(Employee):
#     def __init__(self, name, tool):
#         super().__init__(name)
#         self.tool = tool

# engineer = DataEngineer("Jo","Saw")
# print(engineer.name)
# print(engineer.tool)


# ========================================= Composition ==============

# class DatabaseConnection:
#     def connect(self):
#         print("Connect to a database")

# class DataPipeline:
#     def __init__(self):
#         self.database = DatabaseConnection()

#     def run(self):
#         self.database.connect()
#         print("Running data pipeline")

# pipeline = DataPipeline()
# pipeline.run()


# output:
# Connect to a database
# Running data pipeline


# ========== eg 2 for Composition=================:

# class Engine:
#     def __init__(self, horsepower: int):
#         self.horsepower = horsepower

#     def start(self):
#         return "Vroom! The engine is running."

# class Car:
#     def __init__(self, make: str, model: str, hp: int):
#         self.make = make
#         self.model = model
#         # Composition: The Car class creates and owns an Engine object
#         self.engine = Engine(horsepower=hp) 

#     def start_car(self):
#         # The Car class delegates the starting behavior to the Engine object
#         print(f"Starting the {self.make} {self.model}...")
#         print(self.engine.start())

# # Usage
# my_car = Car(make="Toyota", model="Corolla", hp=139)
# my_car.start_car()

#==========================================================

# myarr = [10,20,30]


# myitterator = iter(myarr)
# print(next(myitterator))
# print(next(myitterator))
# print(next(myitterator))



# def count_up(limit):
#     current = 1
#     while current <= limit:
#         yield current
#         current += 1

# counter = count_up(3) 
# print(next(counter))
# print(next(counter))
# print(next(counter))


# def add_logging(function):
#     def wrapper():
#         print("Starting function")
#         function()
#         print("function finished")
#     return wrapper

# @add_logging
# def greet():
#     print("Hello")

# greet()


# from typing import Optional

# def find_user(user_id: int) -> Optional[str]:
#     if user_id == 1:
#         return "Alice"
#     return None

# print(find_user("ryan"))



# max_retries = 3

# for attempt in range(1, max_retries+1):
#     try:
#         print("Attempt: " + attempt)
#         somefunc()
#         print("Success")
#         exit()
#     except ConnectionError:


# import csv

# with open(
#     "todelete.csv",
#     "r",
#     encoding="utf-8"
# ) as file:

#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)

#========================================================================
# import csv

# with open(
#     "customerwrite.csv",
#     "w",
#     newline="",
#     encoding="utf-8"
# ) as file:

#     fieldnames = [
#         "customer_id",
#         "name",
#         "age"
#     ]

#     writer = csv.DictWriter(
#         file,
#         fieldnames=fieldnames
#     )

#     writer.writeheader()

#     writer.writerow({
#         "customer_id": "C101",
#         "name": "Rahul",
#         "age": 32
#     })

#======================Week 5========================================

# from pathlib import Path

# folder = Path("C:\\Users\\ryant\\Desktop\\bits-2026\\python-course")
# files = list(folder.glob("*.csv"))
# print(files)


#========================================================================

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))

#========================================================================

# import random

# value = random.randint(1,20)
# print(value)

#========================================================================

# import math

# x = 17
# y = 5
# z = math.ceil(x/y)
# print(z)

#========================================================================

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(
#     url,
#     headers={"Accept": "application/json"},
#     timeout=10
# )

# print(response.status_code)
# print(response.json()["title"])


#========================================================================

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# payload = {
#     "title": "API Basics",
#     "body": "Some body",
#     "userId": 1
# }

# response = requests.post(
#     url,
#     json=payload,
#     timeout=10
# )

# print(response.status_code)
# print(response.json()["title"])
# print(response.json()["id"])

#========================================================================


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     data = response.json()
#     print(data["title"])

# except requests.exceptions.Timeout:
#     print("The request timed out")
# except requests.exceptions.HTTPError as error:
#     print("HTTP Error: ", error)
# except requests.exceptions.RequestException as error:
#     print("Request failed: ", error)
# except ValueError:
#     print("The response was not a valid JSON")

#========================================================================

# import os
# import requests

# API_BASE_URL = os.environ["API_BASE_URL"]
# API_TOKEN = os.environ["API_TOKEN"]
# REQUEST_TIMEOUT = 10

# url = API_BASE_URL + "/orders/123"

# headers = {
#     "Authorization": "Bearer {API_TOKEN}"
# }

# response = requests.get(
#     url,
#     headers=headers,
#     timeout=10
# )

# print(response.status_code)

#=========================Access Tokens, Refresh Tokens===============================================


# import uuid
# import time
# import requests

# # 1. Simulate an Auth Server / Token Exchange
# class MockAuthServer:
#     def __init__(self):
#         self.refresh_tokens = set()

#     def login(self, username, password):
#         if username == "admin" and password == "secret":
#             access_token = str(uuid.uuid4())
#             refresh_token = str(uuid.uuid4())
#             self.refresh_tokens.add(refresh_token)
#             return {
#                 "access_token": access_token,
#                 "refresh_token": refresh_token,
#                 "expires_in": 3600
#             }
#         raise ValueError("Invalid credentials")

#     def refresh(self, current_refresh_token):
#         if current_refresh_token in self.refresh_tokens:
#             # In rotation, invalidate the old refresh token and issue a new one
#             self.refresh_tokens.remove(current_refresh_token)
            
#             new_access_token = str(uuid.uuid4())
#             new_refresh_token = str(uuid.uuid4())
#             self.refresh_tokens.add(new_refresh_token)
            
#             return {
#                 "access_token": new_access_token,
#                 "refresh_token": new_refresh_token,
#                 "expires_in": 3600
#             }
#         raise ValueError("Invalid or expired refresh token")

# # --- Example Usage ---
# auth_server = MockAuthServer()

# # Step 1: Initial Login to get Access Token & Refresh Token
# tokens = auth_server.login("admin", "secret")
# print("Initial Login Response:", tokens)

# access_token = tokens["access_token"]
# refresh_token = tokens["refresh_token"]

# # Step 2: Use the access token to call JSONPlaceholder (which accepts any mock data)
# headers = {"Authorization": f"Bearer {access_token}"}
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers)
# print("JSONPlaceholder API Response:", response.json())

# # Step 3: Access token expires, use Refresh Token to get a new pair (Refresh Rotation)
# new_tokens = auth_server.refresh(refresh_token)
# print("Refreshed Tokens Response:", new_tokens)
   


#===========================================================

import time
import requests

BASE_URL = "https://dummyjson.com"

# ==========================================
# 1. INITIAL LOGIN
# ==========================================
print("[*] Logging in with short-lived tokens (1 minute expiry)...")
login_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 1  # DummyJSON minimum window is 1 minute
    },
    headers={"Content-Type": "application/json"}
)

if login_response.status_code != 200:
    print(f"[-] Login Failed: {login_response.text}")
    exit(1)

data = login_response.json()
access_token = data.get("accessToken")
refresh_token = data.get("refreshToken")

print(f"[+] Login Successful!")
print(f"    Access Token:  {access_token[:25]}...")
print(f"    Refresh Token: {refresh_token[:25]}...\n")

# ==========================================
# 2. VALID CALL (Before Expiration)
# ==========================================
print("[*] Accessing protected endpoint /auth/me with FRESH token...")
headers = {"Authorization": f"Bearer {access_token}"}
me_response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
print(f"    Status Code: {me_response.status_code} (Expected: 200)")
print(f"    User Name:   {me_response.json().get('firstName')}\n")

# ==========================================
# 3. FORCE EXPIRATION
# ==========================================
# We sleep for 35 seconds to simulate a short-lived expiration window. 
# Depending on network latency and backend precision, you can increase this 
# to 60+ seconds if DummyJSON strictly enforces the 60-second cutoff.
sleep_duration = 35 
print(f"[*] Sleeping for {sleep_duration} seconds to allow token to age...")
time.sleep(sleep_duration)

# Let's verify that the access token has aged/expired
print("\n[*] Re-trying API with the same token after wait...")
stale_response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
print(f"    Status Code: {stale_response.status_code} (If 401, token expired successfully)")

# ==========================================
# 4. REFRESH THE TOKENS
# ==========================================
print("\n[*] Rotating tokens using the /auth/refresh endpoint...")
refresh_response = requests.post(
    f"{BASE_URL}/auth/refresh",
    json={
        "refreshToken": refresh_token,
        "expiresInMins": 1
    },
    headers={"Content-Type": "application/json"}
)

if refresh_response.status_code != 200:
    print(f"[-] Refresh Failed: {refresh_response.text}")
    exit(1)

refreshed_data = refresh_response.json()
new_access_token = refreshed_data.get("accessToken")
new_refresh_token = refreshed_data.get("refreshToken") # The rotated refresh token

print(f"[+] Token Rotation Successful!")
print(f"    New Access Token:  {new_access_token[:25]}...")
print(f"    New Refresh Token: {new_refresh_token[:25]}...\n")

# ==========================================
# 5. CALL APIS WITH NEW ACCESS TOKEN
# ==========================================
print("[*] Re-attempting API access using the NEW access token...")
new_headers = {"Authorization": f"Bearer {new_access_token}"}
final_response = requests.get(f"{BASE_URL}/auth/me", headers=new_headers)

print(f"    Status Code: {final_response.status_code} (Expected: 200)")
print(f"    User Email:  {final_response.json().get('email')}")
print("[+] Workflow completed successfully.")
