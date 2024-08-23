class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.pos = position
        self.__salary = salary
        self.__annual_salary = None

        # Message for pretty printing is broken up to two parts
        # to make PEP8 happy (otherwise line will be too long)
        self.msg_p1 = f"{self.name} ({self.age}): {self.pos}"
        self.msg_p2 = " [$" + "%.2f" % self.__salary + "]"

    def __str__(self) -> str:
        return self.msg_p1 + self.msg_p2

    def __repr__(self) -> str:
        return str(
            "Employee.Employee("
            + '"'
            + str(self.name)
            + '"'
            + ", "
            + str(self.age)
            + ", "
            + '"'
            + str(self.pos)
            + '"'
            + ", "
            + str(self.__salary)
            + ")"
        )

    def __add__(self, other):
        return [self, other]

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        minimum_wage = 1000
        if new_salary < minimum_wage:
            raise ValueError("Minimum wage is $1000")
        else:
            self.__annual_salary = None
            self.__salary = new_salary

    @property
    def annual_salary(self):
        if self.__annual_salary is None:
            self.__annual_salary = self.salary * 12
        return self.__annual_salary

    def print(self):
        print(self.msg_p1 + self.msg_p2, sep="")

    def increase_salary(self, percent):
        self.__salary += self.__salary * (percent / 100)