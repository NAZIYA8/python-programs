'''
@Author: Naziya
@Date: 19-07-2021
@Last Modified by: Naziya
@Last Modified: 19-07-2021
@Title: Aim of the program is to reverse the order of items in array.
'''

from LoggerFormat import logger
import array

def reverseArray(myArray):
    """
    Description:
        This function is used to display a reversed array.
    Parameter:
        Myarray is for array elements.
    """
    try:
        logger.info("Original array: ")
        logger.info(myArray)
        myArray =myArray[::-1]
        logger.info("Reversed array: ")
        logger.info(myArray)
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[10,20,30,40,50,60,70,80])
        reverseArray(myArray)
    
    except Exception as err:
        logger.error(err)