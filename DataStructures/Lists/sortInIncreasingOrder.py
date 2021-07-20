'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to sort in increasing order
'''

from LoggerFormat import logger

def sortByOrder():
    """
    Description:
        This function is used to get sort list in increasing order 
    """
    try:
        givenList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        return sorted(givenList, key = lambda element:element[1])
    
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    sort = sortByOrder()
    logger.info(sort)