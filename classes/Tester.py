import classes.Employee2 as Employee


class Tester(Employee.Employee):
    def run_tests(self):
        print(f"===> Testing is started by {self.name}...")
        print("===> Testing is done")