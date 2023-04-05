class Account:
    def __init__(self, login, password) -> None:
        self.__login
        self.__password

    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, new_login):
        raise AttributeError("Login is read-only")
    
    @property
    def password(self):
        raise AttributeError("Password is write-only")
    
    @password.setter
    def password(self, new_password):
        self.__password = new_password