import random
import string

from collections import UserList, UserString

from httplib2 import Credentials


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

    @classmethod
    def user_exist(cls, username):

        """
        method that checks if a user exists from the user list
        """

        for user in cls.UserList:
            if user.username == username:
                return True
        return False   

    class Credentials:
        """
        Class that generates a list of credentials
        """

        AccountsList = []

        def __init__(self, accountname, accountusername, accountpassword):

            """
            __init__ method that helps us define properties for our objects.
            """

            self.accountname = accountname
            self.accountusername = accountusername
            self.accountpassword = accountpassword

        def save_account(self):

            """
            save_account method saves account objects into account_list
            """

            Credentials.AccountsList.append(self)

        def delete_account(self):
                
                """
                delete_account method deletes a saved account from the account_list
                """
    
                Credentials.AccountsList.remove(self)

        @classmethod
        def display_accounts(cls):

            """
            method that returns the account list
            """
            for account in cls.AccountsList:
                return cls.AccountsList
        
        @classmethod
        def find_by_number(cls, number):

            """
            method that takes in a number and returns a account that matches that number
            """

            for account in cls.AccountsList:
                if account.accountusername == number:
                    return account
            

        