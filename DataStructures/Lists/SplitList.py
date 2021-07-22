'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to split a list based on first character of word.
'''

from LoggerFormat import logger
from itertools import groupby
from operator import itemgetter

def difference():
    """
    Description:
        This function is used to split a list based on first character of word.
    """
    try:
        list1 = ['be','have','do','say','get','make','go','take','see','come','think',
                'look','give','leave']

        for letter, words in groupby(sorted(list1), key=itemgetter(0)):
            logger.info(letter)
            for word in words:
                logger.info(word)
    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    difference()