import Tester
import Developer


employee1 = Tester.Tester("Victor Tverskoy", 44, 6000)
print(f"Starting conditions for {employee1.name} in our company:\n\t", employee1)
employee1.run_tests()
percent = 20
employee1.increase_salary(percent)
print(f"We increased {employee1.name}'s salary by {percent}%")
print(f"Current conditions for {employee1.name} in our company:\n\t", employee1, "\n")

employee2 = Developer.Developer("Anton Golovin", 30, 7000)
print(f"Starting conditions for {employee2.name} in our company:\n\t", employee2)
employee2.implement_feature()
monthly_bonus = 300
percent = 10
employee2.increase_salary(percent, monthly_bonus)
print(f"We increased {employee2.name}'s salary by {percent}% and added monthly bonus ${monthly_bonus}")
print(f"Current conditions for {employee2.name} in our company:\n\t", employee2)
