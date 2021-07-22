'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is create the colon of a tuple.
'''

from LoggerFormat import logger

def colonOfTuple():
    """
    Description:
        This function is to create the colon of a tuple.
    """

    try:
        tuple1 = (10, "apple ", " mango ", "cake ", 50, 20)
        tuple2 = tuple1
        logger.info(tuple1)
        logger.info(tuple2)

    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    colonOfTuple()