'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to remove a key from a dictionary.
'''

from LoggerFormat import logger

def removeKey():
    """
    Description:
        This function is used to remove a key from dictionary
        using pop method.
    """

    try:
        dict = {'a': 10, 'b': 20, 'c': 30, 'd':40}
        logger.info("Original Dictionary:")
        logger.info(dict)
        dict.pop("b")
        logger.info("Dictionary after removing a key: ")
        logger.info(dict)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    removeKey()