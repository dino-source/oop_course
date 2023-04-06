import Employee


e1 = Employee.Employee("John Smith", 38, "developer", 1200.0)
e1.print()

e2 = Employee.Employee("Jane Croft", 44, "tester", 1000.0)
print(e2)

e2.increase_salary(30)
print(e2)

print(e1)
print(eval(repr(e1)))

employees = e1 + e2
print(employees)

# e1.salary = 990
e2.salary = 1400
print(e2.name, " has $", e2.salary, " monthly salary.", sep='')

# print(e2.__salary)

print(e2.name, " has $", e2.annual_salary, " annual salary.", sep='')