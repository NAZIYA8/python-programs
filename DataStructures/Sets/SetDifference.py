'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is used to get the set difference
'''

from LoggerFormat import logger

def setDifference():
    """
    Description:
        This function is used to get the set difference
    """

    try:
        set1 = {1, "pqr", 2 , 3, "ab", 2, 5}
        set2 = {8, "ab", "mno", 9, 5, 7}
        only_in_set1 = set1.difference(set2)
        only_in_set2 = set2.difference(set1)
        logger.info("Elements only in set1 ")
        logger.info(only_in_set1)
        logger.info("Elements only in set2 ")
        logger.info(only_in_set2)
    
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    setDifference()