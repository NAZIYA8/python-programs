'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to iterate over a dictionary.
'''

from LoggerFormat import logger


def iterate_over_dictionary():
    """
    Description:
        This function is used to iterate over a dictionary.
    """
    try:

        dict = {'a': 10, 'b': 20, 'c': 30, 'd':40}
        print("printing key value pairs:")
        for key, value in dict.items():
            print (key , value)

    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    iterate_over_dictionary()