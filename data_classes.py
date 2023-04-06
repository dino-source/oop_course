from dataclasses import dataclass


@dataclass
class Project:
    name: str
    payment: int
    client: str

@dataclass
class Employee:
    name: str
    age: int
    salary: float
    project: Project

p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)