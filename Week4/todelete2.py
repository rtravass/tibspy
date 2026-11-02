#=============== Type Hints ============

name: str = "ryan"
age: int = 40

#========arguments

def greet(name: str):
    print(f"Hello {name}")

greet("Ryan")

#=======return vals

def add(num1: int, num2: int) -> int:
    return num1 + num2

print(add(3,4))


#============ Type hints for collections

names: list[str] = ["Jerry","Tom"]

scores: dict[str,int] = {
    "Tom": 6,
    "Jerry": 3
}

point: tuple[int,int] = (10,20)


#================ type hints optional

from typing import Optional

def find_user(userid: int) -> Optional[str]:
    if userid == 1:
        return "Found"
    return None


#=========================================

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    is_employee: bool = True

user = User("Ryan", 40)
print(user)


# op: User(name='Ryan', age=40, is_employee=True)



#====================== Enumeration ===================

from enum import Enum

class Status(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3

# Accessing Enum properties
print(Status.PENDING)        # Output: Status.PENDING
print(Status.PENDING.name)   # Output: PENDING
print(Status.PENDING.value)  # Output: 1




#==================== Exception Handling ===================

try:
    number = int("10")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful")
finally:
    print("Operation complete")


try:
    value = int("abc")
except ValueError, TypeError:
    print("Invalid input")



#==================== Custom Exception Handling ===================

class InsufficientBalanceError(Exception):
    pass

balance = 500
amount = 800

try:
    if amount >= balance:
        raise InsufficientBalanceError("Insufficient balance")
except InsufficientBalanceError as error:
    print(error)



#================================= Retry Pattern  =========== 


max_retries = 3

for attempt in range(1, max_retries + 1):
    try:
        print("Attempt: ", attempt)
        connect_to_service()
        print("Success")
        break
    except ConnectionError:
        print("Temporary failure")