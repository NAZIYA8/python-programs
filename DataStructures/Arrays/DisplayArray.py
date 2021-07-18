'''
@Author: Naziya
@Date: 19-07-2021
@Last Modified by: Naziya
@Last Modified: 19-07-2021
@Title: Aim of the program is to create array of 5 integers and display array items
        with index values.
'''

from LoggerFormat import logger
import array

def displayArray(myArray):
    """
    Description:
        This method is used to create array of 5 integers and displaying array items
        using index values.
    Parameter:
        Myarray is for array elements.
       
    """
    try:

        for i in range(len(myArray)):
            logger.info(myArray[i])
           
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    
    try:
        myArray = array.array("i",[10,20,30,40,50])
        displayArray(myArray)
    
    except Exception as err:
        logger.error(err)