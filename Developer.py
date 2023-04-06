import Employee2


class Developer(Employee2.Employee):
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus