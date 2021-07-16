'''
@Author: Naziya
@Date: 16-07-2021
@Last Modified by: Naziya
@Last Modified Time: 16-07-2021
@Title: Aim of the program is testing the User details.
'''

class RegexPattern:

    firstName_pattern = "^[A-Z]{1}[a-z]{3,}"
    lastName_pattern = "^[A-Z]{1}[a-z]{3,}"
    mobileNumber_pattern = "^[0-9]{2}\\s{1}[0-9]{10}"
    email_pattern = "^[a-zA-Z0-9]+([+.-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,4}([.][a-zA-Z]{2,4})?"
    password_pattern = "^(?=.*[A-Z])(?=.*\\d)(?=.*?[!@#$%^&*?=-]).{8,}$"
    zipCode_pattern = "[0-9]{6}$"
    