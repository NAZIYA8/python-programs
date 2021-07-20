'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to remove elements from list
'''

from LoggerFormat import logger

def removeElements():
    """
    Description:
        This function is used to remove elements from list
    """

    try:
        givenList =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        del givenList[0]
        givenList.remove('Pink')
        givenList.pop() 
        logger.info("Elements after removing: ")
        logger.info(givenList)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    removeElements()