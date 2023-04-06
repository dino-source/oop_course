class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    @property
    def salary(self) -> float:
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        # minimum_wage = 1000
        if new_salary < 1000:
            raise ValueError("Minimum wage is $1000")
        else:
            self.__salary = new_salary


print(Employee.__dict__)