import classes.Developer as Developer
import classes.Tester as Tester


def main():
    ioc = "in our company"
    emp1 = Tester.Tester("Victor Tverskoy", 44, 6000)
    print(f"Starting conditions for {emp1.name} {ioc}:\n\t", emp1)
    emp1.run_tests()
    percent = 20
    emp1.increase_salary(percent)
    print(f"We increased {emp1.name}'s salary by {percent}%")
    print(f"Current conditions for {emp1.name} {ioc}:\n\t", emp1, "\n")

    emp2 = Developer.Developer("Anton Golovin", 30, 7000, "Qt")
    print(f"Starting conditions for {emp2.name} {ioc}:\n\t", emp2)
    emp2.implement_feature()
    print(f"{emp2.name} uses {emp2.framework} in his day-to-day work.")
    monthly_bonus = 300
    percent = 10
    emp2.increase_salary(percent, monthly_bonus)
    msg_p1 = f"We increased {emp2.name}'s salary by {percent}% "
    msg_p2 = f"and added monthly bonus ${monthly_bonus}"
    print(msg_p1 + msg_p2)
    print(f"Current conditions for {emp2.name} {ioc}:\n\t", emp2)


main()