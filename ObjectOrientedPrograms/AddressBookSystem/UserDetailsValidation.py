'''
@Author: Naziya
@Date: 13-07-2021
@Last Modified by: Naziya
@Last Modified Time: 16-07-2021
@Title: Aim of the program is AddressBook Problem using oops concept.
'''

from LoggerFormat import logger
import re

class ValidateDetails:


    def validateFirstName():
        """
    Description:
        This method is used for  validating first name with regex pattern.
    Return:
        It returns a valid first name .
       
    """
        
        try:
            while True:
                user_fname = input(" Enter Your First Name : ")
                if re.match("^[A-Z]{1}[a-z]{4,}$",user_fname):
                    return user_fname
                else:
                    logger.error("Starting of name should be capital and length should be minimum of 4 characters ")
                    

        except ValueError:
            logger.error("Invalid input")


    def validateLastName():
        """
    Description:
        This method is used for  validating last name with regex pattern.
    Return:
        It returns a valid last name.
       
    """
        
        try:
            while True:
                user_lname = input(" Enter Your Last Name : ")
                if re.match("^[A-Z]{1}[a-z]{4,}$", user_lname):
                    return user_lname
                else:
                    logger.error("Starting of name should be capital and length should be minimum of 4 characters ")
                    

        except ValueError:
            logger.error("Invalid input")        

    def validateNumber():
        """
    Description:
        This method is used for validating mobile number with regex pattern.
    Return:
        It returns a valid mobile number.
       
    """
        try:
            while True:
                    user_phone = input(" Enter Your Mobile Number : ")
                    if re.match("^[0-9]{2}\\s{1}[0-9]{10}", user_phone):
                        return user_phone
                    else:
                        logger.error("Mobile number should be in this format (+91-8235465768) ")
                        
        except ValueError:

            logger.error("Invalid input")


    def validateZipcode():
        """
    Description:
        This method is used for  validating zipcode with regex pattern.
    Return:
        It returns a valid zipcode.
       
    """
        try:
            while True:
                    user_zip = input(" Enter Your zipcode : ")
                    if re.match("[0-9]{6}$", user_zip):
                        return user_zip
                    else:
                        logger.error("Enter a valid zipcode")
                        
        except ValueError:
            print("Invalid input")

    
    def validateAddress():
        """
    Description:
        This method is used for  validating address with regex pattern.
    Return:
        It returns a valid address.
       
    """
        try:
            while True:
                    user_address = input(" Enter Your Address : ")
                    if re.match("[a-zA-Z0-9]*$", user_address):
                        return user_address
                    else:
                        logger.error("Enter a Valid address Name ")
                        
        except ValueError:
            logger.error("Invalid input")

    def validateCity():
        """
    Description:
        This method is used for  validating city name with regex pattern.
    Return:
        It returns a valid city name.
       
    """
        try:
            while True:
                    user_city = input(" Enter Your City Name : ")
                    if re.match("[a-zA-Z]*$", user_city):
                        return user_city
                    else:
                        logger.error("Enter valid City name")
                        
        except ValueError:

            logger.error("Invalid input")

    
    def validateState():
        """
    Description:
        This method is used for validating state name with regex pattern.
    Return:
        It returns a valid state name.
       
    """
        try:
            while True:
                    user_state = input(" Enter Your State name : ")
                    if re.match("[a-zA-Z]*$", user_state):
                        return user_state
                    else:
                        logger.error("Enter valid state name")
                        
        except ValueError:

            logger.error("Invalid input")

    