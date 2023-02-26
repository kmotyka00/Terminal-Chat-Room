import sys
sys.path.append('../src')
import unittest
from users_management import UsersManager

class TestUserManagement(unittest.TestCase):

    def test_create_users_table(self):
        users_manager = UsersManager()
        users_manager.create_users_table()
        
        c = users_manager.connection.cursor()
        users_table_exists = c.execute(''' SELECT name FROM sqlite_master WHERE type='table' AND name='users'; ''').fetchone()

        self.assertEqual(len(users_table_exists), 1)

    def test_register(self):
        users_manager = UsersManager()
        users_manager.register()
    
    def test_login(self):
        users_manager = UsersManager()
        users_manager.login()


if __name__ == "__main__":
    unittest.main()