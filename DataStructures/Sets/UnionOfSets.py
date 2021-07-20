'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is used for the union of sets
'''

from LoggerFormat import logger

def unionOfSet():
    """
    Description:
        This function is used for the union of sets
    """

    try:
        set1 = {1, "pqr", 2 , 3, "ab", 2, 5}
        set2 = {8, "ab", "mno", 9, 5, 7}
        logger.info("After union of set1 and set2: ")
        resultSet= set1.union(set2)
        logger.info(resultSet)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    unionOfSet()