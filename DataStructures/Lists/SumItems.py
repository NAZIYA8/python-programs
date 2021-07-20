'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to get sum of all items in list.  
'''

from LoggerFormat import logger

def sumAllItems():
    """
    Description:
        This function is used to get sum of all items in list  
    """

    try:
        list = [1,2,3,4,5]
        logger.info("Sum of all items in list: ")
        logger.info(sum(list))

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    sumAllItems()