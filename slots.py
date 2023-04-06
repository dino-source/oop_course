class Developer:
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

    def has_slots(self):
        return hasattr(self, "__slots__")

employee1 = Developer("Juliana Craine", 38, 1000, "Flask")
print(employee1.__slots__)
print(f"Check if Developer class has slots:", employee1.has_slots())