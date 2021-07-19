'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to sort in ascending and descending order.
'''

from LoggerFormat import logger

def sortDictionary():
    """
    Description:
        This function is used to sort in ascending and descending order.
    """

    try:
        dict ={'a': 1, 'c': 2, 'd': 3, 'x': 4, 'e': 5}
        logger.info("sorting in ascending order: ")
        ascending = sorted(dict.items(), key=lambda  element: element[1])
        logger.info(ascending)
        logger.info("sorting in descending order: ")
        descending = sorted(dict.items(), key=lambda  element: element[1], reverse=True)
        logger.info(descending)
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    sortDictionary()