'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to convert a list to tuple
'''

from LoggerFormat import logger

def listToTuple():
    """
    Description:
        This function is to to convert a list to tuple
    """

    try:
        listItems = [1,3,6,9,7]
        logger.info(tuple(listItems))
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    listToTuple()