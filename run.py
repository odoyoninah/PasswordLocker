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




