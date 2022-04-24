from collections import UserList


class User:
    UserList = []
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        UserList.append(self)