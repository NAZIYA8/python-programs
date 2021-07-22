'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to get the last part of a string before a specified character.
'''

from LoggerFormat import logger

def getLastPart():
    """
    Description:
        This function is to get the last part of a string before a specified character.
    """

    try:
        string1 = "https://www.w3resource.com/python-exercises"
        
        logger.info(string1.rsplit('-', 1)[0])
    
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    getLastPart()