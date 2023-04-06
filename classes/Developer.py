import classes.Employee2 as Employee


class Developer(Employee.Employee):
    __slots__ = ("framework", )

    def __init__(self, name: str, age: int, salary: float, framework: str = '') -> None:
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent: float, bonus: float = 0):
        super().increase_salary(percent)
        self.salary += bonus

    def implement_feature(self):
        print(f"===> Feature development is started by {self.name}...")
        print("===> Feature has been implemented. Development is done.")