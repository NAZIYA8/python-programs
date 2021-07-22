'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to take input from the user and displays that input back in
        upper and lower cases.
'''

from LoggerFormat import logger

def upperLowerCase():
    """
    Description:
        This function is to take input from the user and displays that 
        input back in upper and lower cases.
    """

    try:
        logger.info("String in lowercase: ")
        logger.info(string1.lower())
        logger.info("String in uppercase: ")
        logger.info(string1.upper())
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    string1 = input("Enter a string ")
    upperLowerCase()
