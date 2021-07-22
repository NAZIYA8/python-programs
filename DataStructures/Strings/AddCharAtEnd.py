'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to add 'ing' at the end of a given string or 
        with ly if it ends with ing.
'''

from LoggerFormat import logger

def addAtEnd(string1):
    """
    Description:
        This function is to add 'ing' at the end of a given string or 
        with ly if it ends with ing.
    """

    try:
        if len(string1) < 3:
            logger.info("Length of string must be more than 3 ")
        else:
            if string1.endswith("ing"):
                string1 += "ly"
            else:
                string1 +="ing"
            logger.info(string1)
    except Exception as err:
        logger.info(err)

if __name__ == "__main__":
    string1 = input("Enter a string ")
    addAtEnd(string1)