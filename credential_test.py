'''
import uniittest to create uniittests for Password Locker Module
import Password Locker Module to be tested
'''
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create credential object
        self.new_credential = Credential("doe","Yahoo","yahoo17")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        Credential.credential_list = []

    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''
        self.assertEqual( self.new_credential.user_password, "doe")
        self.assertEqual( self.new_credential.credential_name, "Yahoo" )
        self.assertEqual( self.new_credential.credential_password, "yahoo17" )

    def test_save_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''

        # Save the new credential
        self.new_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 1 )

    def test_save_multiple_credentials(self):
        '''
        Test case to test if you can save multiple objects to credential list
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("doe2","Facebook","facebook17")

        test_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 2)

    def test_generate_password(self):
        '''
        Test case to test if a user can log into their credentials
        '''
        
        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 8 )   
    
    def test_display_credential(self):
        '''
        Test case to test if a user can see a list of all the credentials saved
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("doe2","Facebook","facebook17")

        test_credential.save_credential()

        test_credential = Credential("doe2","Yahoo","yahoo17")

        test_credential.save_credential()
        
        self.assertEqual( len(Credential.display_credential("doe2")) , 2 )
        
    def test_credential_exist(self):
        
        '''
        Test to check if we can return a boolean if we can't find the credential
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("doe2","Facebook","facebook17")

        test_credential.save_credential()
        
        # use contact exist method
        credential_exists = Credential.credential_exist("Facebook")
        
        self.assertTrue(credential_exists)
        

if __name__ == '__main__':
    unittest.main()