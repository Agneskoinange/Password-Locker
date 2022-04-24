#!/usr/bin/env python3.8

'''
This is the file that runs the application
Import User Class from User Module and Credential Class from Credential Module
'''
from user import User
from credential import Credential

def create_user(name, password):
    '''
    Function to create a user account
    Args:
        name : the name the user wants for the account
        password : the password the user want for the account
    '''

    new_user = User(name,password)

    return new_user

def save_users(user):
    '''
    Function to save a user account
    Args:
        user : the user account to be saved
    '''

    user.save_user()

def check_existing_users(name):
    '''
    Function that checks if a user account name already exists
    Args:
        name : the user account name
    '''

    return User.user_exist(name)

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)

def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()

def create_credentail(user_password, name, password):
    '''
    Function to create a credential 
    Args:
        user_password : the password for Password Locker
        name : the name of the account 
        password : the password for the account
    '''

    new_credentail = Credential(user_password,name,password)

    return new_credentail

def save_credentials(credential):
    '''
    Function to save a credential
    Args:
        credential : the credential to be saved
    '''

    credential.save_credential()

def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists
    Args:
        name : the credential name
    '''

    return Credential.credential_exist(name)

def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credential.display_credential(password)

def create_generated_password(name):
    '''
    Function that generates a password for the user 
    Args:
        name : the name of the account
    '''
    password = Credential.generate_password()

    return password

def main():
    '''
    Function running the Password Locker app
    '''

    print('''Welcome to Password Locker \n
Use these short codes to get around''')

    while True:
        '''
        Loop that is running the entire application
        '''

        print('''   Short codes:
        cu - create a Password Locker account \n
        du - display names of current Password Locker users \n
        lg - log into your Password Locker account \n
        ex - exit the Password Locker account''')

        # Get short codes from the user
        short_code = input().lower()

        if short_code == 'cu':
            '''
            Creating a Password Locker account
            '''

            print("\n")
            print("New Password Locker Account")
            print("-"*10)

            print("User name ...")
            user_name = input()

            print("Password ...")
            user_password = input()

            # Create and save new user
            save_users( create_user( user_name, user_password) )

            print("\n")
            print(f"{user_name} welcome to Password Locker")
            print("\n")

        elif short_code == 'du':
            '''
            Display the names of the current users 
            '''

            if display_users():
                print("\n")
                print("Here are the current users of Password Locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be the first user :)")
                print("\n")

        elif short_code == 'lg':
            '''
            Logs in the user into their Password Locker account
            '''
            print("\n")
            print("Log into Password Locker Account")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in(user_name,user_password) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                user_log_in(user_name,user_password)
                print("\n")
                print(f'''{user_name} welcome to your Credentials\n
                Use these short codes to get around''')

                while True:
                    '''
                    Loop to run functions after logging in
                    '''
                    print('''  Short codes:
        cc - add a credential \n
        dc - display credentials \n
        cg - create a credential with a generate password \n
        ex - exit Credentials''')

                    # Get short code from the user
                    short_code = input().lower()

                    if short_code == 'cc':
                        '''
                        Creating a Credential
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        # Create and save new user
                        save_credentials( create_credentail( user_password, credential_name, credential_password) )

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                   
if __name__ == '__main__':
    main()
