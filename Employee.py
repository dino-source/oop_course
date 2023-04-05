class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.__salary = salary

    def __str__(self) -> str:
        return f"{self.name} ({self.age}): {self.position} [$" + "%.2f" % self.__salary + "]"
    
    def __repr__(self) -> str:
        return str(
            'Employee.Employee(' +
            '\"' + str(self.name) + '\"' + ', ' +
            str(self.age) + ', ' +
            '\"' + str(self.position) + '\"' + ', ' +
            str(self.__salary) + ')'
        )
    
    def __add__(self, other):
        return [self, other]
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        minimum_wage = 1000
        if new_salary < minimum_wage:
            raise ValueError("Minimum wage is $1000")
        else:
            self.__salary = new_salary

    @property
    def annual_salary(self):
        return self.salary * 12

    def print(self):
        print(f"{self.name} ({self.age}): {self.position} [$", "%.2f" % self.__salary, "]", sep='')

    def increase_salary(self, percent):
        self.__salary += self.__salary * (percent/100)