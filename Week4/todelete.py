#========================== Simple Class ===========================
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(self.name, self.email)

customer1 = Customer("ryan","ryan@gmail.com")
customer1.display_info()

#============================= Inheritance ===========================

class Employee:
    def login(self):
        print("Employee logged in")

class DataEngineer(Employee):
    def build_pipeline(self):
        print("Building Data Pipeline")

engineer = DataEngineer()
engineer.login()
engineer.build_pipeline()



# op:
# Employee logged in
# Building Data Pipeline


#============================= Method Overriding ===========================

class Employee:
    def work(self):
        print("Employee is working")

class DataEngineer(Employee):
    def work(self):
        print("Data Engineer is building pipeline")

emp1 = Employee()
emp2 = DataEngineer()
emp1.work()
emp2.work()

# op:
# Employee is working
# Data Engineer is building pipeline


#============================= use super() to reuse parent logic ===========================

class Employee:
    def __init__(self, name):
        self.name = name

class DataEngineer(Employee):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

eng1 = DataEngineer("ryan","python")
print(eng1.name)
print(eng1.tool)


# op:
# ryan
# python

#=========================== iterable, iterator ==========================

numbers  = [1,2,3,4,5]
numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

# op:
# 1
# 2
# 3
# 4
# 5
# StopIteration


#=========================== Custom iterator ==========================

class CountUp:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


counter = CountUp(3)
print(next(counter))
print(next(counter))
print(next(counter))

# op:
# 1
# 2
# 3
# StopIteration


#======================= Generators and yeild ==========================

def countup(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

counter = countup(3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# op:
# 1
# 2
# 3
# StopIteration

#===

squares = [x * x for x in range(10)]
print(squares)

squares2 = (x * x for x in countup(10))
print(next(squares2))
print(next(squares2))
print(next(squares2))


# op2:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 1
# 4
# 9


#========================= Decorator ==========================

def greet():
    print("Hello")

newfunc = greet  # function can be passed like objects
newfunc()

# op:
# Hello


#===============Decorator for logging ======================

def add_logging(myfunction):
    def mywrapper():
        print("Starting function")
        myfunction()
        print("Ending function")
    return mywrapper

@add_logging
def greet():
    print("Hello")

greet()

# op:
# Starting function
# Hello
# Ending function


#===============Decorator for timing ======================

import time

def timer(myfunc):
    def mywrapper():
        start = time.time()
        myfunc()
        end = time.time()
        print("Time: ", end - start)
    return mywrapper

@timer
def greet():
    print("Hello")

greet()

# op:
# Hello
# Time:  0.00012874603271484375