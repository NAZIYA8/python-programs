'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to remove item if present from a set
'''

from LoggerFormat import logger

def removeMemberIfPresent():
    """
    Description:
        This function is used to remove item if present from a set
    """

    try:
        mySet = {1, "pqr", 2 , 3, "ab", 2, 5}
        logger.info("Original Set")
        logger.info(mySet)
        logger.info("Set after removing items")
        if "pqr" in mySet:
            mySet.remove("pqr")
        logger.info(mySet)
    
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    removeMemberIfPresent()