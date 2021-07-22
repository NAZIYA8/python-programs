'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to count the number of characters in string
'''

from LoggerFormat import logger

def countCharacters():
    """
    Description:
        This function is to count the number of characters in string
    """

    try:
        myString = "google.com"
        frequency = {}
        for char in myString:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        logger.info(frequency)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    countCharacters()