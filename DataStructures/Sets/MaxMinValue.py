'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to find maximum and minimum item in the set
'''

from LoggerFormat import logger

def setMaxMin():
    """
    Description:
        This function is used to find maximum and minimum item in the set
    """

    try:
        mySet = {1, 2 , 3, 4, 5, 6}
        logger.info("Minimum of set :")
        logger.info(min(mySet))
        logger.info("Maximum of set :")
        logger.info(max(mySet))
    
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    setMaxMin()