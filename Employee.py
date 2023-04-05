class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def print(self):
        print(f"{self.name} ({self.age}): {self.position} [$", "%.2f" % self.salary, "]", sep='')

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)