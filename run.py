from username import User
from username import Credentials

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

def find_account_by_number(number):
    """
    Function that finds an account by number and returns the account
    """
    return Credentials.find_by_number(number)

def display_accounts():
    """
    Function that returns the account list
    """
    return Credentials.display_accounts()

def main():
    while True:
        print("Hello! Welcome to Password Locker. What is your name?")
        user_name = input()
        print(f"Hello {user_name}. What would you like to do?")
        print('\n')
        print("Use these short codes : cc - create a new user account, da - display accounts, fa - find an account, ex - exit the user list.")
        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Username ...")
            u_name = input()

            print("Password ...")
            p_word = input()

            save_user(create_user(f_name, l_name, u_name, p_word))

        



