'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to add a key to dictionary.
'''

from LoggerFormat import logger


def add_key_to_dictionary():
    """
    Description:
        This function is used to add a key to dictionary.
    """

    try:
        dict_elements = {0:10, 1:20}
        dict_elements[2] = 30
        logger.info("New dictionary elements are : ")
        logger.info(dict_elements)
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    add_key_to_dictionary()