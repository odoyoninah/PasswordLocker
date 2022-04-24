import unittest
from username import User

class TestUsername(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    
        unittest.TestCase: TestCase class that helps in creating test cases
    """

def setUp(self):
    """
    Set up method to run before each test cases.
    """
    self.new_user = User("Annapurna", "Nins", "Nina45", "12345")  

def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_user.firstname, "Annapurna")
    self.assertEqual(self.new_user.lastname, "Nins")
    self.assertEqual(self.new_user.username, "Nina45")
    self.assertEqual(self.new_user.password, "12345")

def test_save_user(self):
    """
    test_save_user test case to test if the user object is saved into
    the user list
    """
    self.new_user.save_user()  
    self.assertEqual(len(User.display_users()), 1)

def test_delete_user(self):
    """
    test_delete_user test case to test if the user object is deleted from
    the user list
    """
    self.new_user.save_user()
    test_user = User("Annapurna", "Nins", "Nina45", "12345")  
    test_user.save_user()

    self.new_user.delete_user()  
    self.assertEqual(len(User.display_users()), 1)

if __name__ == '__main__':
    unittest.main()