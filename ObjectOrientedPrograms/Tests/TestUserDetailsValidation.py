'''
@Author: Naziya
@Date: 16-07-2021
@Last Modified by: Naziya
@Last Modified Time: 16-07-2021
@Title: Aim of the program is testing the User details.
'''

import unittest
from UserDetailsValidation import ValidateDetails as validate

class TestUserDetailsValidation(unittest.TestCase):


    def test_whenGivenValidFirstName_shouldReturnTrue(self):
        """
        Description:
            The given valid first name should return true in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertTrue(validate.validateFirstName("Naziya"))
        self.assertTrue(validate.validateFirstName("Naz"))


    def test_whenGivenInvalidFirstName_shouldReturnFalse(self):
        """
        Description:
            The given Invalid first name should return false in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertFalse(validate.validateFirstName("naziya"))
        self.assertFalse(validate.validateFirstName("Na"))
        self.assertFalse(validate.validateFirstName("Na45"))
        self.assertFalse(validate.validateFirstName("Na*#zi"))


    def test_whenGivenValidLastName_shouldReturnTrue(self):
        """
        Description:
            The given valid last name should return true in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertTrue(validate.validateLastName("Syeda"))
        self.assertTrue(validate.validateLastName("Sye"))


    def test_whenGivenInvalidLastName_shouldReturnFalse(self):
        """
        Description:
            The given Invalid last name should return false in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertFalse(validate.validateLastName("syeda"))
        self.assertFalse(validate.validateLastName("Sy"))
        self.assertFalse(validate.validateFirstName("sy45"))
        self.assertFalse(validate.validateFirstName("Sy*e@"))


    def test_whenGivenValidMobileNumber_shouldReturnTrue(self):
        """
        Description:
            The given valid mobile number should return true in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertTrue(validate.validateNumber("91 9645897521"))

    def test_whenGivenInvalidMobileNumber_shouldReturnFalse(self):
        """
        Description:
            The given Invalid mobile number should return false in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertFalse(validate.validateNumber("9166966"))
        self.assertFalse(validate.validateNumber("91914586259852"))
        self.assertFalse(validate.validateNumber("919876543210"))

    def test_whenGivenValidEmail_shouldReturnTrue(self):
        """
        Description:
            The given valid Email should return true in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertTrue(validate.ValidateEmail("abc10@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc-100@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc.100@yahoo.com"))
        self.assertTrue(validate.ValidateEmail("abc111@abc.com"))
        self.assertTrue(validate.ValidateEmail("abc-100@abc.net"))
        self.assertTrue(validate.ValidateEmail("abc.100@abc.com.au"))
        self.assertTrue(validate.ValidateEmail("abc@1.com"))
        self.assertTrue(validate.ValidateEmail("abc@gmail.com.com"))
        
    def test_whenGivenInvalidEmail_shouldReturnFalse(self):
        """
        Description:
            The given Invalid Email should return false in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertFalse(validate.ValidateEmail("Naziya@.com"))
        self.assertFalse(validate.ValidateEmail("nazi@gmail"))
        self.assertFalse(validate.ValidateEmail("abc..28@gmail.com"))
        self.assertFalse(validate.ValidateEmail("abc123@gmail.c"))
        self.assertFalse(validate.ValidateEmail("abc@abc@gmail.com"))
        self.assertFalse(validate.ValidateEmail("abc@gmail.com.aa.au"))


    def test_whenGivenValidPassword_shouldReturnTrue(self):
        """
        Description:
            The given valid password should return true in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertTrue(validate.validatePassword("Jac&9iwol"))
        self.assertTrue(validate.validatePassword("j&cks6H1hd"))

        
    def test_whenGivenInvalidPassword_shouldReturnFalse(self):
        """
        Description:
            The given Invalid password should return false in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertFalse(validate.validatePassword("Jsfiu74hd"))
        self.assertFalse(validate.validatePassword("J&ckschd"))
       
    def test_whenGivenValidZipCode_shouldReturnTrue(self):
        """
        Description:
            The given valid ZipCode should return true in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertTrue(validate.validateZipcode("560056"))
        

    def test_whenGivenInvalidZipCode_shouldReturnFalse(self):
        """
        Description:
            The given Invalid ZipCode should return false in the test case
        Parameter:
            It takes self as a parameter.
        """

        self.assertFalse(validate.validateZipcode("5265"))