class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self) -> str:
        return f"{self.name} ({self.age}): monthly salary $" + "%.2f" % self.salary
    
    def __repr__(self) -> str:
        return str(
            'Employee2.Employee(' +
            '\"' + str(self.name) + '\"' + ', ' +
            str(self.age) + ', ' +
            str(self.salary) + ')'
        )