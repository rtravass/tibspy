company_name = "ABC Technologies"

def calculate_salary(basic_salary, allowance, deduction):
    net_salary = basic_salary + allowance - deduction
    return net_salary

def calculate_bonus(basic_salary, performance):
    bonus = basic_salary * performance / 100
    return bonus

calculate_tax = lambda salary, tax_rate: salary * tax_rate / 100

# Main program
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction = float(input("Enter deduction: "))
performance = float(input("Enter performance percentage: "))

net_salary = calculate_salary(basic_salary, allowance, deduction)
bonus = calculate_bonus(basic_salary, performance)
tax = calculate_tax(net_salary + bonus, 10)
final_salary = net_salary + bonus - tax

print("\n============Salary Details ===========")
print(f"Company: {company_name}")
print(f"Basic Salary: {basic_salary}")
print(f"Allowance: {allowance}")
print(f"Deduction: {deduction}")
print(f"Performance_Bonus: {bonus}")
print(f"Tax: {tax}")
print("\n======================================")
print(f"Final Salary: {final_salary}")