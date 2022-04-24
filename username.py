from collections import UserList, UserString


class User:
    """
    Class that generates a list of users
    """

    UserList = []

    def __init__(self, firstname, lastname, username, password):

        """
        ___init___method for user class
        """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.UserList.append(self)


    def delete_user(self):
        User.UserList.remove(self)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.username} {self.password}"

    UserList = []
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

        def save_user(self):

        User.UserList.append(self)