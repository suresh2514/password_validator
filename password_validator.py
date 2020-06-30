"""
Write a Python Program to generate a  logic for Password validator
  1. Using Classes and Objects
  2. Log all the Events
  3. Write Positive and Negative TestCases
"""

#%% password.py
from getpass import getpass
import logging
import re

class PasswdValidate:
    def __init__(self, passwd):
        self.passwd = passwd

    def minchar(self, min=8):
        return(len(self.passwd) >= min)

    def alphanum(self):
        if re.search('[\d]+', self.passwd):
            if re.search('[A-Z,a-z]', self.passwd):
                return True
        return False

    def special(self):
        if re.search('[\W]', self.passwd):
            return True
        return False


if __name__ == '__main__':
    logging.basicConfig(filename='passwd.debug', level=logging.DEBUG)
    password = getpass()
    _password=PasswdValidate(password)
    if not _password.minchar():
        logging.info("Password is of less than 8 character")
    if not _password.alphanum():
        logging.info("Password does not have alpha numeric character")
    if not _password.special():
        logging.info("Password does not have special character")


#%% testunit
import unittest
from password import PasswdValidate


good_password=PasswdValidate("test@123$%")
bad_password=PasswdValidate("abcxyz")

class PasswdValidateTest(unittest.TestCase):
    def test_minchar(self):
        self.assertEqual(True, good_password.minchar())
        self.assertEqual(False, bad_password.minchar())

    def test_alphanum(self):
        self.assertEqual(True, good_password.alphanum())
        self.assertEqual(False, bad_password.alphanum())

    def test_special(self):
        self.assertEqual(True, good_password.special())
        self.assertEqual(False, bad_password.special())


if __name__ == '__main__':
    unittest.main()
