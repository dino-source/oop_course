import Employee2


class Developer(Employee2.Employee):
    def __init__(self, name, age, salary, framework) -> None:
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

    def implement_feature(self):
        print(f"===> Feature development is started by {self.name}...")
        print("===> Feature has been implemented. Development is done.")