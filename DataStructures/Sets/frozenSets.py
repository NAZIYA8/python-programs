'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to create a frozenset
'''

from LoggerFormat import logger

def createFrozenSet():
    """
    Description:
        This function is used to create frozenset
    """

    try:
        mySet = frozenset({1, "pqr", 2 , 3, "ab", 2, 5})
        logger.info(mySet)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    createFrozenSet()