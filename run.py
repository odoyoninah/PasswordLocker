import string
from random import choice
from user import User
from user import Credentials

def create_user(firstname, lastname, username, password):
    """
    Function to create a new user
    """
    new_user = User(firstname, lastname, username, password)
    return new_user

def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()

def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

def display_users():
    """
    Function that returns the user list
    """
    return User.display_users()

def find_user_by_number(number):
    """
    Function that finds a user by number and returns the user
    """
    return User.find_by_number(number)

def create_account(accountname, accountusername, accountpassword):
    """
    Function to create a new account
    """
    new_account = Credentials(accountname, accountusername, accountpassword)
    return new_account

def save_account(account):
    """
    Function to save a new account
    """
    account.save_account()

def delete_account(account):
    """
    Function to delete an account
    """
    account.delete_account()




