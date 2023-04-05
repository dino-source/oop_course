employee1 = {
    "name" : "Ji-Soo",
    "age" : 38,
    "position" : "developer",
    "salary" : 1200,
}

employee2 = {
    "name" : "Lauren",
    "age" : 44,
    "position" : "tester",
    "salary" : 1000,
}

def increase_salary(employee, percent):
    employee["salary"] += employee["salary"] + (percent/100)

def employee_info(employee):
    print(
        f"{employee['name']} is {employee['age']} years old. " +
        f"The employee is a {employee['position']} with " +
        f"salary of ${employee['salary']}")

employees = [employee1, employee2]

for employee in employees:
    employee_info(employee)
