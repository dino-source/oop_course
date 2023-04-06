class SlotInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, "__slots__")
    
    
class Employee():
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

class Developer(SlotInspectorMixin, Employee):
    __slots__ = ("framework", )

    def __init__(self, name, age, salary, framework='') -> None:
        super().__init__(name, age, salary)
        self.framework = framework

employee1 = Developer("Juliana Craine", 38, 1000, "Flask")
print(employee1.__slots__)
print(f"Check if Developer class has slots:", employee1.has_slots())
print(employee1.__dict__)
