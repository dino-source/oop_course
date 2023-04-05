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

employees = [employee1, employee2]

for emp in employees:
    print(f"{emp['name']}'s salary is ${emp['salary']}")
