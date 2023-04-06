from dataclasses import dataclass


@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    def notify_client(self):
        print(f"Notify the client about the progress of the {self.name}...")

@dataclass(slots=True)
class Employee:
    name: str
    age: int
    salary: float
    project: Project

p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)

p.notify_client()