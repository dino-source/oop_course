class Developer:
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

employee1 = Developer("Juliana Craine", 38, 1000, "Flask")
print(employee1.__slots__)