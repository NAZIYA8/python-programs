'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to slice a tuple
'''

from LoggerFormat import logger

def sliceTuple():
    """
    Description:
        This function is to slice a tuple
    """

    try:
        tuple1 = (1,2,3,4,5,6,7,8)
        logger.info(tuple1[::-1])
        logger.info(tuple1[2::2])
        logger.info(tuple1[1:5])
        logger.info(tuple1[-7:-3:])
    
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    sliceTuple()
