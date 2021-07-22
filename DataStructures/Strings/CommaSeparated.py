'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to accepts a comma separated sequence of words as input
        and prints the unique words in sorted form (alphanumerically)..
'''

from LoggerFormat import logger

def commaSeparated():
    """
    Description:
        This function is to accepts a comma separated sequence of words as input
        and prints the unique words in sorted form (alphanumerically).
    """

    try:
        items = input("Input comma separated sequence of words")
        words = [word for word in items.split(",")]
        result = ",".join(sorted(list(set(words))))
        logger.info(result)

    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    commaSeparated()