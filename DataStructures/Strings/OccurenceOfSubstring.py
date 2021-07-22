'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to count occurrences of a substring in a string.
'''

from LoggerFormat import logger

def occurenceOfSubstring(data,findSub):
    """
    Description:
        This function is to count occurrences of a substring in a string.
    """

    try:
        logger.info(data.count(findSub))
    except Exception as err:
        logger.error(err)

## driver code
data = input("Enter sentence")
findSub = input("Enter Substring")
occurenceOfSubstring(data,findSub)