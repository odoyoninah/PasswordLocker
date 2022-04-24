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

        """
        delete_user method deletes a saved user from the user_list
        """

        User.UserList.remove(self)

    @classmethod
    def display_users(cls):

        """
        method that returns the user list
        """

        return cls.UserList

    @classmethod
    def find_by_number(cls, number):

        """
        method that takes in a number and returns a user that matches that number
        """

        for user in cls.UserList:
            if user.username == number:
                return user    