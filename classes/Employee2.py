class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self) -> str:
        ms = "monthly salary"
        return f"{self.name} ({self.age}): {ms} $" + "%.2f" % self.salary

    def __repr__(self) -> str:
        return f"Employee2.Employee({self.name}, {self.age}, {self.salary})"