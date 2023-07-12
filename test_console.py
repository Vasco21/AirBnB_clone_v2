#!/usr/bin/python3

import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_do_create(self):
        args = "create BaseModel name='test object' number=42"
        expected_output = "test object\n"
        
        with StringIO() as output, StringIO(args) as input:
            sys.stdout = output
            sys.stdin = input
            self.console.onecmd("{}".format(args))
            self.assertEqual(output.getvalue(), expected_output)

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__


if __name__ == '__main__':
    unittest.main()
