'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to reverse a tuple
'''

from LoggerFormat import logger

def reverseTuple():
    """
    Description:
        This function is to reverse a tuple
    """

    try:
        tuple1 = (1,2,3,4,5,6,7,8)
        logger.info("Reversed Tuple:")
        logger.info(tuple1[::-1])
        
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    reverseTuple()
