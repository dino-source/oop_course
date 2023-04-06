import Tester
import Developer


employee1 = Tester.Tester("Victor Tverskoy", 44, 6000)
print(employee1)
employee1.run_tests()

employee2 = Developer.Developer("Anton Golovin", 30, 7000)
print(f"\nStarting conditions for {employee2.name} in our company:\n\t", employee2)

monthly_bonus = 1300
employee2.increase_salary(10, monthly_bonus)
print(f"\nWe increased {employee2.name}'s salary by 10% and added monthly bonus ${monthly_bonus}")
print(f"Current conditions for {employee2.name} in our company:\n\t", employee2)
