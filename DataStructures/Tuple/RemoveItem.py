'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to remove an item from a tuple.
'''

from LoggerFormat import logger

def removeItem():
    """
    Description:
        This function is to to remove an item from a tuple.
    """

    try:
        tuple1 = (1,9,3,4,6,5)
        listElements = list(tuple1)
        result = listElements.pop(2)
        logger.info(result)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    removeItem()