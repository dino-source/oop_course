class Person:
    def __init__(self, first_name, last_name, id) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.id = id

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def first_name(self):
        pass

    @first_name.getter
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @property
    def last_name(self):
        pass

    @last_name.getter
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name