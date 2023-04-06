class Person:
    def __init__(self, first_name, last_name, id) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = id

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

