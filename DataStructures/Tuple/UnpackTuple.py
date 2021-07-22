'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to unpack a tuple in several variables
'''

from LoggerFormat import logger

def unpackTuple():
    """
    Description:
        This function is to unpack a tuple in several variables
    """

    try:
        x, y, *z = (10, "apple ", " mango ", "cake ", 50, 20)
        logger.info(x)
        logger.info(y)
        logger.info(z)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    unpackTuple()