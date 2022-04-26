'''
Import random and string modules from Python for generating passwords
# Import User from user module to get access to a user
'''
from random import choice
import string
# from user import User

'''
Credential class : for creating a credentials for a user
'''

class Credential:
    '''
    Class that generates instances of a users credentials
    '''

    # Empty list of credentials
    credential_list = []

    def __init__(self, user_password, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        Args:
            user_password : password of the user
            credential_name : name of an account
            credential_password : password for the account
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    def save_credential(self):
        '''
        Method that saves a user's credentials to credential list
        '''
        Credential.credential_list.append(self)

    # def delete_credential(self):

    #     '''
    #     delete_contact method deletes a saved credentials from the credentials_list
    #     '''

    #     Credential.credential_list.remove(self)

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        # Length of the generated password
        size = 8

        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password

    @classmethod
    def display_credential(cls,password):
        '''
        Method that returns the credential list
        Args:
            password : the user password
        '''
        user_credential_list = []

        for credential in cls.credential_list:
            if credential.user_password == password:
                user_credential_list.append(credential)

        return user_credential_list
    
    @classmethod
    def credential_exist(cls, name):
        
        '''
        Method that checks if a credential exists in the credential list
        
        Args:
            name: name of the credential to search
            
        Returns:
            Boolean: true/false depending if the contact exists
            
        '''
        
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return True
            
        return False
