employee1 = {
    "name" : "Ji-Soo",
    "age" : 38,
    "position" : "developer",
    "salary" : 1200.0,
}

employee2 = {
    "name" : "Lauren",
    "age" : 44,
    "position" : "tester",
    "salary" : 1000.0,
}
def init_employee(name, age, position, salary):
    return {
        "name" : name,
        "age" : age,
        "position" : position,
        "salary" : salary,
    }

employee3 = init_employee("Mateo", 38, "developer", 2000)

def increase_salary(employee, percent):
    employee["salary"] += employee["salary"] * (percent/100)

def employee_info(employee):
    print(
        f"{employee['name']} is {employee['age']} years old. " +
        f"The employee is a {employee['position']} with " +
        f"salary of ${employee['salary']}")

employees = [employee1, employee2]

increase_salary(employee2, 20)
for employee in employees:
    employee_info(employee)
