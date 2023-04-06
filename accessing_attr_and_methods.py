class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.__salary = salary

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
            raise ValueError("Company is bankrupt.")
        elif new_wage < Employee.__minimum_wage:
            raise ValueError("Minimum wage is $" + "%.2f" % Employee.__minimum_wage)
        else:
            cls.__minimum_wage = new_wage

    def increase_salary(self, percent):
        new_salary = self.__salary + self.__salary * (percent/100.0)
        if new_salary > Employee.__maximum_wage:
            raise ValueError(
                f"We cannot pay to our employees ${new_salary} per month, " +
                "because it will cause us to go bankrupt")
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
            raise ValueError("Minimum wage is $" + "%.2f" % Employee.__minimum_wage)
        elif new_salary > Employee.__maximum_wage:
            raise ValueError(
                f"We cannot pay to our employees ${new_salary} per month, " +
                "because it will cause us to go bankrupt")
        else:
            self.__salary = new_salary


print(Employee.__dict__)

e = Employee("John Smith", 38, 7000.00)
print("Before:", e)
Employee.__dict__["increase_salary"](e, 10)
print("After1:", e)

# e.increase_salary(100)
# print("After2:", e)

print(f"Minimum wage is ${Employee.minimum_wage()}")
print(f"Maximum wage is ${Employee.maximum_wage()}")