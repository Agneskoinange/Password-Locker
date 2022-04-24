'''
import uniittest to create uniittests for User Module
import User Module to be tested
'''
import unittest
from user import User
from credential import Credential


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User Class behaviours
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create user object
        self.new_user = User("John","doe")


    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        User.user_list = []

    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.user_name, "John" )
        self.assertEqual( self.new_user.user_password, "doe" )

    def test_save_user(self):
        '''
        Test case to test if the user object is saved into the user list
        '''

        # Saving the new user
        self.new_user.save_user()

        self.assertEqual( len(User.user_list), 1 )

    def test_save_multiple_users(self):
        '''
        Test case to test if you can save multiple objects to user list
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Jane","doey")

        test_user.save_user()

        self.assertEqual( len(User.user_list), 2)

    def test_find_credential(self):
        '''
        Test case to test if the User module is importing from Credential module
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Jane","doey")

        test_user.save_user()

        found_credential = User.find_credential("Yahoo")

        self.assertEqual( found_credential, False )

    def test_log_in(self):
        '''
        Test case to test if a user can log into their credentials
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Jane","doey")

        test_user.save_user()

        found_credential = User.log_in("Jane", "doey")

        self.assertEqual( found_credential,  Credential.credential_list )   
    
    def test_display_user(self):
        '''
        Test case to test if a user can see a list of all the users saved
        '''
        
        self.assertEqual( User.display_user() , User.user_list )
        
    def test_user_exist(self):
        
        '''
        Test to check if we can return a boolean if we can't find the user
        '''
        
        # Save the new user
        self.new_user.save_user()

        test_user = User("Jane","doey")

        test_user.save_user()
        
        # use contact exist method
        user_exists = User.user_exist("Jane")
        
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main(verbosity=2)