
# ========================= Sorted with Lambda =======================
products = [
    ("laptop",50000),
    ("car",600000),
    ("mobile",40000)
]

sorted_products  = sorted(products, key = lambda item: item[1])
print(products)
print(sorted_products)

result:
[('laptop', 50000), ('car', 600000), ('mobile', 40000)]
# [('mobile', 40000), ('laptop', 50000), ('car', 600000)]

# =========================# =========================# =========================   





# ========================= Filter with Lambda =======================

scores = [30,40,50,60,70,80,10]

high_scores = list(filter(lambda x: x > 60,scores))
print(high_scores)

result:
[70, 80]
# =========================# =========================# =========================   



# ========================= Map with Lambda =======================
price = [100,200,300]
print(price)

updated_price = list(
        map(lambda x: x * 1.1,price)
    )
print(updated_price)

result:
[100, 200, 300]
[110.00000000000001, 220.00000000000003, 330.0]

# =========================# =========================# ========================= 

def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(10, 3)
print(result)



===============================Tuple ========================================


transaction = ("ryan travasso","IDBI",5000)
print(transaction[2])

name,bank,amount = transaction
print(name)

# op:
# 5000
# ryan travasso


=============================== Set ===========================================

employees = {"v1014151","v1014152","v1014153"}
employees.add("v1014154")
print(employees)      #print order may differ
employees.remove("v1014153")

week1 = {"Sunday","Monday","Tuesday"}
week2 = {"Tuesday","Monday","Wednesday"}
print(week1 | week2)
print(week1 & week2)



===============================Dictionary ========================================

emp = {
    "v1014151":"ryan",
    "v1014152":"jose"
}

emp["v1014153"] = "jay"
emp["v1014153"] = "om"

print(emp.get("v1014151"))

for key in emp:
    print(key)

for key,val in emp.items():
    print(key, ":",val)





=============================== File Operations ========================================


try:
    with open("customer_details.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Customer Details file not found")
else:
    print("Operation completed successfully")
finally:
    print("Closed")


=============================


from pathlib import Path

filepath = Path("Week3/reviews.csv")
print(filepath.exists())
print(filepath.is_file())
print(filepath.is_dir())


# #Creating Directories
outputdir = Path("newfolder")
outputdir.mkdir(exist_ok=True)   #dont raise an error if already exists
print(outputdir.exists())
print(outputdir.is_dir())


#Checking PAths
datadir = Path("C:\\Users\\ryant\\Desktop\\bits-2026\\python-course\\Week3")
print(datadir.name)
for filepath in datadir.iterdir():
    if filepath.is_file():
        print(filepath.name)
        print(filepath.suffix)

======================= csv file operations ==================================

import csv

# with open("EmployeeData.csv","r") as file:
#     reader = csv.DictReader(file)

    # for row in reader:   #reads a CSV file and maps each row into a dictionary
    #     print(row["First_Name"],row["Last_Name"],row["Department"])
    #     if float(row["Salary"]) > 90000:
    #         print(row["First_Name"])

with open("EmployeeData.csv","r",newline="") as file:
    reader = csv.DictReader(file)

    with open("Updated_EmployeeData.csv","w",newline="") as opfile:
        colnames=["Employee_ID","First_Name","Updated_Salary"]
        writer = csv.DictWriter(opfile,fieldnames=colnames)
        writer.writeheader()

        for row in reader:
            updated_salary = float(row["Salary"]) * 1.10
            writer.writerow({
                "Employee_ID": row["Employee_ID"],
                "First_Name": row["First_Name"],
                "Updated_Salary": updated_salary
            }
        )

# Output:
# Employee_ID,First_Name,Updated_Salary
# 101,John,104500.00000000001
# 102,Jane,93500.00000000001
# 103,Michael,68200.0

========================Week 4 ============================================


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