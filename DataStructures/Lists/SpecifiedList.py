'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to print a specified list after removing the 0th, 4th and
        5th elements.
'''

from LoggerFormat import logger

def specifiedList():
    """
    Description:
        This function is used to print a specified list after removing the 0th, 
        4th and 5th elements.
    """
    try:
        myList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        count = 0
        myList.__delitem__(0 - count)
        count += 1
        myList.__delitem__(4 - count)
        count += 1
        myList.__delitem__(5 - count)
        count += 1
        logger.info(myList)

    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    specifiedList()