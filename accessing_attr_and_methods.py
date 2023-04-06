class Employee:
    __minimum_wage = 1000

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self) -> str:
        return f"{self.name} ({self.age}): monthly salary $" + "%.2f" % self.salary

    @property
    def salary(self) -> float:
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < Employee.__minimum_wage:
            raise ValueError("Minimum wage is $" + "%.2f" % Employee.__minimum_wage)
        else:
            self.__salary = new_salary


print(Employee.__dict__)

e = Employee("John Smith", 38, 1000.00)
print("Before:", e)
Employee.__dict__["increase_salary"](e, 20)
print("After:", e)
