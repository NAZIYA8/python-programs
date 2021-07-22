'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to reverse string
'''

from LoggerFormat import logger

def reverseString():
    """
    Description:
        This function is to reverse string
    """

    try:
        string1 = input("enter string")
        reversed = string1[::-1]
        logger.info("Reversed String:")
        logger.info(reversed)
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    reverseString()