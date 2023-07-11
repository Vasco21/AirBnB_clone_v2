import unittest
import MySQLdb
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        # Connect to the MySQL database
        self.db = MySQLdb.connect(host='localhost',
                                  user='hbnb_test',
                                  passwd='hbnb_test_pwd',
                                  db='hbnb_test_db')

        # Create a cursor object
        self.cursor = self.db.cursor()

        # Create the HBNBCommand instance
        self.console = HBNBCommand()

        # Disable stdout during the tests
        self.console.disable_stdout()

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_state(self):
        # Get the initial number of records in the states table
        self.cursor.execute('SELECT COUNT(*) FROM states')
        initial_count = self.cursor.fetchone()[0]

        # Execute the create command
        self.console.onecmd('create State name="California"')

        # Get the final number of records in the states table
        self.cursor.execute('SELECT COUNT(*) FROM states')
        final_count = self.cursor.fetchone()[0]

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

if __name__ == '__main__':
    unittest.main()
