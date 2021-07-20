'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to clone list
'''

from LoggerFormat import logger

def cloneList():
    """
    Description:
        This function is used to clone list
    """
    try:
        originalList = [1,2,"abc","22"]
        newList = list(originalList)
        logger.info("Original list :")
        logger.info(originalList)   
        logger.info("New list :")
        logger.info(newList) 
   
    except Exception as err:
        print(err)

if __name__ == "__main__":
    cloneList()