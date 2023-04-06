import Employee2
import Developer
import Tester


employee1 = Tester.Tester("Victor Tverskoy", 44, 6000)
print(isinstance(employee1, Tester.Tester))
print(isinstance(employee1, Employee2.Employee))

employee2 = Developer.Developer("Anton Golovin", 30, 7000)
print(issubclass(Developer.Developer, Employee2.Employee))
print(issubclass(Employee2.Employee, object))
print(issubclass(Developer.Developer, object))