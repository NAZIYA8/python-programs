'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to check if element exist in a tuple
'''

from LoggerFormat import logger

def elementCheck():
    """
    Description:
        This function is to check if element exist in a tuple
    """

    try:
        tuple1 = (10, 4, 5, 6, 8)
        element = 5
        result = element in tuple1
        logger.info(result)

    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    elementCheck()