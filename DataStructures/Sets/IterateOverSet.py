'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to iterate over a set
'''

from LoggerFormat import logger

def iterateSet():
    """
    Description:
        This function is used to iterate over a set
    """
    try:
        mySet = {1, "pqr", 2 , 3, "ab", 2, 5}
        for element in mySet:
            logger.info(element)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    iterateSet()