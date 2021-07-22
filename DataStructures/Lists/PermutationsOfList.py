'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to generate all permutations of a list
'''

from LoggerFormat import logger
import itertools

def permutation():
    """
    Description:
        This function is used to generate all permutations of a list
    """
    try:
        myList = [1, 2, 3]
        permutationsObject = itertools.permutations(myList)
        permutationsList = list(permutationsObject)
        logger.info(permutationsList)

    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    permutation()