'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to find the length of the string
'''

from LoggerFormat import logger

def stringLength():
    """
    Description:
        This function is to find the length of the string
    """

    try:
        myString = "pineapple"
        stringLength = len(myString)
        logger.info(stringLength)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    stringLength()   