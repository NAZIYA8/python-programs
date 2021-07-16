'''
@Author: Naziya
@Date: 16-07-2021
@Last Modified by: Naziya
@Last Modified Time: 16-07-2021
@Title: Aim of the program is testing the User details.
'''

from LoggerFormat import logger
import re
from RegexPattern import RegexPattern as re_pattern

class ValidateDetails:


    def validateFirstName(firstNameInput):
        """
    Description:
        This method is used for  validating first name with regex pattern.
    Return:
        It returns True if its valid first name.
        It returns False if its Invalid first name.
       
    """
        
        try:
            if re.match(re.compile(re_pattern.firstName_pattern),firstNameInput):
                return True
            else:
                return False

        except Exception as err:
            logger.error(err)


    def validateLastName(lastNameInput):
        """
    Description:
        This method is used for  validating last name with regex pattern.
    Return:
        It returns True if its valid last name.
        It returns False if its Invalid last name.
       
    """
        try:
            if re.match(re.compile(re_pattern.lastName_pattern),lastNameInput):
                return True
            else:
                return False

        except Exception as err:
            logger.error(err)
        


    def validateNumber(mobileNumberInput):
        """
    Description:
        This method is used for validating mobile number with regex pattern.
    Return:
        It returns True if its valid mobile.
        It returns False if its Invalid mobile.
       
    """
        try:
            if re.match(re.compile(re_pattern.mobileNumber_pattern),mobileNumberInput):
                return True
            else:
                return False

        except Exception as err:
            logger.error(err)



    def validateZipcode(zipCodeInput):
        """
    Description:
        This method is used for validating zipcode with regex pattern.
    Return:
        It returns True if its valid ZipCode.
        It returns False if its Invalid ZipCode.
       
    """
        try:
            if re.match(re.compile(re_pattern.zipCode_pattern),zipCodeInput):
                return True
            else:
                return False

        except Exception as err:
            logger.error(err)


    def validateEmail(emailInput):
        """
    Description:
        This method is used for validating email with regex pattern.
    Return:
        It returns True if its valid email.
        It returns False if its Invalid email.
       
    """
        try:
            if re.match(re.compile(re_pattern.email_pattern),emailInput):
                return True
            else:
                return False

        except Exception as err:
            logger.error(err)


    def validatePassword(passwordInput):
        """
    Description:
        This method is used for validating password with regex pattern.
    Return:
        It returns True if its valid password.
        It returns False if its Invalid password.
       
    """
        try:
            if re.match(re.compile(re_pattern.password_pattern),passwordInput):
                return True
            else:
                return False

        except Exception as err:
            logger.error(err)
