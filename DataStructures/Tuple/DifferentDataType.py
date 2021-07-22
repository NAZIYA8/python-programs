'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to create a tuple of different data types
'''

from LoggerFormat import logger

def createTuple():
    """
    Description:
    This function is used to create a tuple of different data types
    """

    try:
        tuple1 = tuple(['apple','banana', True, 1, 85, 35.8]) 
        logger.info(tuple1)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    createTuple()
