'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to lowercase first n characters in a string.
'''

from LoggerFormat import logger

def lowerCase(data):
    """
    Description:
        This function is to lowercase first n characters in a string.
    """

    try:
        logger.info(data[:4].lower() +data[4:])
    except Exception as err:
        logger.error(err)

## driver code
data = input("Enter the string")
lowerCase(data)