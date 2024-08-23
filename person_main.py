import classes.Person as Person


def main():
    p1 = Person.Person("Roger", "Glover", 1234)

    p1.first_name = "Glen"
    p1.last_name = "Huges"
    print(p1.full_name)


main()