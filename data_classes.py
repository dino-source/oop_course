class Project:
    def __init__(self, name, payment, client) -> None:
        self.name = name
        self.payment = payment
        self.client = client

    def __repr__(self) -> str:
        return (
            f"Project" +
            f"(name={repr(self.name)}, " + 
            f"payment={repr(self.payment)}, " +
            f"client={repr(self.client)})"
        )

class Employee:
    def __init__(self, name, age, salary, project) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)