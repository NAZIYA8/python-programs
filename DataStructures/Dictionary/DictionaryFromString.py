'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to create dictionary from string.
'''

from LoggerFormat import logger

def dictionaryFromString():
    """
    Description:
        This function is used to create a dictionary from a string.
    """

    try:
        dict = {}
        string = 'w3resource'
            
        logger.info(string)    
        for character in string:
            dict[character] = string.count(character)
        logger.info("Dictionary from string: ")
        logger.info(dict)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    dictionaryFromString()