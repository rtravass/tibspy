# from pathlib import Path

# folder = Path("data")
# files = list(folder.glob("*.csv"))
# print(files)

#==========================================================

# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))

#==========================================================

# import random

# value = random.randint(1,20)
# print(value)

#==========================================================

# import math 

# x = 17
# y = 5

# z = math.ceil(x/y)
# print(z)

#==================  GET   ================================

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(
#     url,
#     headers={"Accept": "application/json"},
#     timeout=0
# )

# print(response.status_code)
# print(response.json()["title"])


#==================  POST   ================================

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# payload = {
#     "title": "API Basics",
#     "body": "Learning HTTP requests",
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

#================== 


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     data = response.json()
#     print(data["title"])

# except requests.exceptions.Timeout:
#     print("The request has timed out")

# except requests.exceptions.HTTPError as error:
#     print("HTTP error: ", error)

# except requests.exceptions.RequestException as error:
#     print("Request failed", error)

# except ValueError:
#     print("The response is not a valid Json")



#================== API tokens ========================

# import requests
# import os

# os.environ["API_BASE_URL"] = "https://jsonplaceholder.typicode.com"   # Set env variable
# os.environ["API_TOKEN"] = "abcde123456"

# print(os.environ["API_TOKEN"])

# url = os.environ["API_BASE_URL"] + "/orders/123"

# headers = {
#     "Authorization": f"Bearer {os.environ['API_TOKEN']}"
# }

# response = requests.get(
#     url,
#     headers = headers,
#     timeout = 10
# )

# print(response.status_code)



#========================= Reuseable API Client ==========================

# import os
# import requests

# API_BASE_URL = os.environ["API_BASE_URL"]
# API_TOKEN = os.environ["API_TOKEN"]
# REQUEST_TIMEOUT = 10

# def get_order(order_id):
#     url = f"{API_BASE_URL}/orders/{order_id}"

#     headers = {
#         "Authorization": f"Bearer {API_TOKEN}"
#     }

#     response = requests.get(
#         url,
#         headers= headers,
#         timeout= REQUEST_TIMEOUT
#     )

#     response.raise_for_status()
#     return response.json()


# def describe_order(order):
#     order_id = order["id"]
#     status = order["status"]

#     return f"Order {order_id} is {status}"


# order_data = get_order(123)
# message = describe_order(order_data)

# print("message")




#===================== Python Automation =================

# from pathlib import Path

# input_dir = Path("C:/Users/rtravass/Desktop/bits/bits-2026/python-course")
# file_path = input_dir/"todelete.csv"

# print(file_path)
# print(file_path.exists())


#=============keep paths and settings separate from processing logic==========

# from pathlib import Path

# INPUT_DIR = Path("")
# OUTPUT_DIR = Path("")

# OUTPUT_DIR.mkdir(parents=True, exist_ok= True)

# print(INPUT_DIR)
# print(OUTPUT_DIR)
# print(OUTPUT_DIR.is_dir())


#=========reusable script =========================

# from pathlib import Path

# INPUT_DIR = Path("")
# OUTPUT_DIR = Path("")

# def validate_input(file_path):
#     if not file_path.is_file():
#         raise FileNotFoundError(
#             f"Input file not found: {file_path}"
#         )
#     return file_path

# def prepare_output():
#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# input_file = validate_input(INPUT_DIR/ "sales.csv")
# prepare_output()

# print("Input validated: ", input_file.name)
# print("Output directory ready: ", OUTPUT_DIR.is_dir())



#================divide a large dataset into manageable batches =======

# records = list(range(1, 11))
# batch_size = 3

# for start in range(0, len(records), batch_size):
#     batch = records[start: start + batch_size]
#     print(batch)

# op:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10]



#===================handle individual record failures ================

# records = [10, 20, 50, -10]
# success = []
# failed = []

# for record in records:
#     try:
#         if record < 0:
#             raise ValueError("Negative amount")
#         success.append(record)

#     except ValueError as error:
#         failed.append(record)
#         print(f"Failed: {record} -> {error}")

# print("Successful: ", success)
# print("Failed records: ", failed)


# op:
# Failed: -10 -> Negative amount
# Successful:  [10, 20, 50]
# Failed records:  [-10]


#================ log outcomes and avoid unnecessary reprocessing =============

# records = [100, 200, 100, 300, 200]
# processed = set()

# for record in records:
#     if record in processed:
#         print(f"Skipped: {record}")
#         continue

#     processed.add(record)
#     print(f"Processed: {record}")


# op:
# Processed: 100
# Processed: 200
# Skipped: 100
# Processed: 300
# Skipped: 200



#======================== generate consolidated output =============

# records = [100, 200, 100, 300, 200]
# results = []
# failed = []

# for record in records:
#     try:
#         if record < 0:
#             raise ValueError("Negative value")
        
#         results.append(record * 2)

#     except ValueError:
#         failed.append(record)

# print("Results: ", results)
# print("Failed: ", failed)
# print("Total successful: ", len(results))



#=================python threading for io bound tasks=================

# import threading
# import time

# def fetch_data(name):
#     print(f"Starting {name}")
#     time.sleep(2)
#     print(f"Finished {name}")

# threads = []

# for name in ["A", "B", "C"]:
#     t = threading.Thread(
#         target=fetch_data, args=(name, )  #target=func to execute, 
#     )                                   #args=supplies func argument as tuple
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join() # * `.join()` tells the main program to **wait** until that specific thread finishes its work before moving on. 

# print("All tasks completed")
        

#=================python threading for io bound tasks=================

# from multiprocessing import Process
# import os

# def calculate(number):
#     total = sum( i * i for i in range(number))
#     print(f"PID {os.getpid}: total = {total}")

# if __name__ == "__main__":
#     process = []

#     for _ in range(2):
#         p = Process(target=calculate, args=(1_00_00, ))
#         process.append(p)  
#         p.start()   #This tells the operating system to actually launch the process and execute the calculate function. It does not block the main code

#     for p in process:
#         p.join()  #This tells the main program to stop and wait for this specific process to finish executing before moving forward. Without join(), the main program might print "All processes completed" while the workers are still running in the background.

#     print("All processes completed")


# op:
# PID 8432: total = 333283335000
# PID 8433: total = 333283335000
# All processes completed



#===================Asynchronous Programming with asyncio ================

# import asyncio

# async def get_data():
#     print("Starting request")
#     await asyncio.sleep(2)
#     print("Request completed")

# asyncio.run(get_data())

# op:
# Starting request
# Request completed


# Four terms form the foundation of asyncio .
# Coroutine. An asynchronous unit of work, defined with async def . It can pause and resume at
# await points.

# async def . Defines an asynchronous function. Calling it creates a coroutine object; it does not
# run the function to completion straight away.

# await . Waits for an awaitable operation and lets the current coroutine pause while other tasks
# progress.

# Event loop. Coordinates the ready tasks and resumes each one when the operation it awaited
# can continue.



#=====================================

# import asyncio

# async def fetch_data(name):
#     print(f"Starting {name}")
#     await asyncio.sleep(2)
#     print(f"Finished {name}")
#     return f"Data from {name}"

# async def main():
#     results = await asyncio.gather(
#         fetch_data("A"),
#         fetch_data("B"),
#         fetch_data("C")
#     )
#     print(results)

# asyncio.run(main())

# op:
# Starting A
# Starting B
# Starting C
# Finished A
# Finished B
# Finished C
# ['Data from A', 'Data from B', 'Data from C']

# fetch_data prints a starting message, awaits a two second sleep to simulate waiting for a network
# response, then prints a finishing message and returns a string. In main , asyncio.gather() receives
# three calls, each of which creates a coroutine object, and the await in front of it waits until all three
# have finished and collects their results.
# All three starting messages appear before any finishing message, because each task reaches its
# await and hands the event loop a chance to run the others. The three waits overlap, so the whole
# run typically takes close to two seconds rather than six. This is one possible output. 


# Note four
# points:
# gather() runs the awaitables concurrently.
# The three asynchronous waits can overlap.
# The order of the finishing messages is not guaranteed.
# The results list keeps the order in which the awaitables were supplied, which is why it reads A,
# B, C.


#=================Handling errors in asynchronous tasks ===

# import asyncio

# async def fetch_data(name):
#     try:
#         await asyncio.sleep(1)
#         if name == "B":
#             raise RuntimeError("Request failed")
#         return f"Data from {name}"
#     except RuntimeError as error:
#         return f"Error for {name} : {error}"

# async def main():
#     results = await asyncio.gather(
#         fetch_data("A"),
#         fetch_data("B"),
#         fetch_data("C")
#     )
#     print(results)

# asyncio.run(main())


# op:
# ['Data from A', 'Error for B : Request failed', 'Data from C']

