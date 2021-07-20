'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to get smallest number from list 
'''

from LoggerFormat import logger

def smallestNumber():
    """
    Description:
        This function is used to get smallest number from list 
    """

    try:
        list = [20, 40, 30, 80, 50]
        logger.info("Smallest Number from list")
        logger.info(min(list))
    
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    smallestNumber()