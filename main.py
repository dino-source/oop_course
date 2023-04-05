import Employee


e1 = Employee.Employee("John Smith", 38, "developer", 1200.0)
e1.print()

e2 = Employee.Employee("Jane Croft", 44, "tester", 1000.0)
e2.print()

e2.increase_salary(30)
e2.print()
