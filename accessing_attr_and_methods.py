from datetime import date

from classes.MathUtils import MathUtils


class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.__salary = salary

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        x = (now.month, now.day) < (dob.month, dob.day)
        age = now.year - dob.year - x
        return cls(name, age, cls.__minimum_wage)

    __minimum_wage = 1000
    __maximum_wage = 10000

    @classmethod
    def minimum_wage(cls) -> int:
        return cls.__minimum_wage

    @classmethod
    def maximum_wage(cls) -> int:
        return cls.__maximum_wage

    @classmethod
    def change_the_minimum_wage(cls, new_wage):
        if new_wage > Employee.__maximum_wage:
            raise ValueError(
                f"It is impossible to apply ${new_wage} as maximum wage. "
                + "It can't be more than $"
                + "%.2f" % Employee.__maximum_wage
            )
        elif new_wage < Employee.__minimum_wage:
            raise ValueError(
                f"It is impossible to apply ${new_wage} as minimum wage. "
                + "It can't be less than $"
                + "%.2f" % Employee.__minimum_wage
            )
        else:
            cls.__minimum_wage = new_wage

    def increase_salary(self, percent):
        new_salary = self.__salary + self.__salary * (percent / 100.0)
        if new_salary > Employee.__maximum_wage:
            msg_p1 = f"We cannot pay to our employees ${new_salary} per month,"
            msg_p2 = " because it will cause us to go bankrupt"
            raise ValueError(msg_p1 + msg_p2)
        else:
            self.__salary = new_salary

    def __str__(self) -> str:
        return f"{self.name} ({self.age}): monthly salary $" + "%.2f" % self.__salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < Employee.__minimum_wage:
            raise ValueError(
                f"It is impossible to apply ${new_salary} salary. "
                + "It can't be less than minimum wage, "
                + "which is $"
                + "%.2f" % Employee.__minimum_wage
            )
        elif new_salary > Employee.__maximum_wage:
            raise ValueError(
                f"We cannot pay to our employees ${new_salary} per month, " + "because it will cause us to go bankrupt"
            )
        else:
            self.__salary = new_salary


# print(Employee.__dict__)

e1 = Employee("John Smith", 38, 7000.00)
print("Before:", e1)
Employee.__dict__["increase_salary"](e1, 10)
print("After1:", e1)

# e.increase_salary(100)
# print("After2:", e)

print(f"Minimum wage is ${Employee.minimum_wage()}")
print(f"Maximum wage is ${Employee.maximum_wage()}")

# Employee.change_the_minimum_wage(200)
# Employee.change_the_minimum_wage(30000)

e2 = Employee.new_employee("Cindy Crawford", date(1966, 2, 20))
print()
print(e2.name)
print(e2.age)
print(e2.salary)

result = MathUtils.divide(3, 2)
print(f"MathUtils.divide(3, 2) = {result}")