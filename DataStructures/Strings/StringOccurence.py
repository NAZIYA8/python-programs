'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to program to get a string from a given string where all
        occurrences of its first char have been changed to '$', except the first char itself.
'''

from LoggerFormat import logger

def stringOccurence():
    """
    Description:
        This function is to program to get a string from a given string where
        all occurrences of its first char have been changed to '$', except the 
        first char itself.
    """

    try:
        string1 = "restart"
        char = string1[0]
        string1 = string1.replace(char, '$')
        string1 = char + string1[1:]
        logger.info(string1)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    stringOccurence()