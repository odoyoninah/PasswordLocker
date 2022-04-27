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

def find_user_by_username(username):
    """
    Function that finds a user by username and returns the user
    """
    return User.find_by_username(username)

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

def existing_account(name):
    """
    Function that checks if an account exists and returns a Boolean
    """
    return Credentials.find_by_account(name)

def find_account(accountname):
    """
    Function that finds an account by accountname and returns the account
    """
    return Credentials.find_by_account(accountname)

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
        print("Use these short codes : ca - create a new user account, da - display accounts, ex - exit the user list, fa-find an account, del - delete an account")
    
        short_code = input().lower()

        if short_code == 'ca':
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
            print('\n')

            print(f"New User {f_name} {l_name} created")
            print('\n')

        elif short_code == 'da':
            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.firstname} {user.lastname} .....{user.username}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'fa':
            print("Enter the username of the account you want to find")
            option = input()
            if existing_account(option):
                search_account = find_account(option)
                print(f"{search_account.accountname} {search_account.accountusername} {search_account.accountpassword}")
                print('-' * 20)

            # search_accountname = input()
            # if find_account(search_accountname):
            #     search_account = find_account(search_accountname)
            #     print(f"{search_account.accountname} {search_account.accountusername} .....{search_account.accountpassword}")
        elif short_code == 'del':
            print("Enter the username of the account you want to delete")
            option = input()
            if existing_account(option):
                delete_account(option)
                print(f"{option} deleted")
                print('\n')
            else:
                print("That account does not exist")
                print('\n')

        elif short_code == 'ex':
            print("Bye .......")
            break

        else:
            print("I really didn't get that. Please use the short codes")
                

       
            
if __name__ == '__main__':
    main()

        



