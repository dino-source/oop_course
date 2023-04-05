class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} ({self.age}): {self.position} [$" + "%.2f" % self.salary + "]"
    
    def __repr__(self) -> str:
        return str(
            'Employee.Employee(' +
            '\"' + str(self.name) + '\"' + ', ' +
            str(self.age) + ', ' +
            '\"' + str(self.position) + '\"' + ', ' +
            str(self.salary) + ')'
        )
    
    def __add__(self, other):
        return [self, other]

    def print(self):
        print(f"{self.name} ({self.age}): {self.position} [$", "%.2f" % self.salary, "]", sep='')

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)