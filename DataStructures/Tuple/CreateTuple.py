'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to create a tuple
'''

from LoggerFormat import logger

def createTuple():
    """
    Description:
        This function is used to create a tuple 
    """

    try:
        tuple1 = tuple({'apple','banana'})
        logger.info(tuple1)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    createTuple()