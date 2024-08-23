import classes.Developer as Developer
import classes.Employee2 as Employee
import classes.Tester as Tester


def main():
    employee1 = Tester.Tester("Victor Tverskoy", 44, 6000)
    print(isinstance(employee1, Tester.Tester))
    print(isinstance(employee1, Employee.Employee))

    employee2 = Developer.Developer("Anton Golovin", 30, 7000)
    print(isinstance(employee2, Developer.Developer))
    print(isinstance(employee2, Employee.Employee))

    print(issubclass(Developer.Developer, Employee.Employee))
    print(issubclass(Employee.Employee, object))
    print(issubclass(Developer.Developer, object))


main()