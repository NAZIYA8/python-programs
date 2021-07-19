'''
@Author: Naziya
@Date: 19-07-2021
@Last Modified by: Naziya
@Last Modified: 19-07-2021
@Title: Aim of the program is to remove the first occurrence of element
        in array
'''

import array
from LoggerFormat import logger

def RemoveFirstOccurence(myArray):
    """
    Description:
        This function is used to find number of occurence of element in array
    Parameter:
        Myarray is for array elements.
       
    """
    try:
        myArray.remove(int(input("Enter the number you want whose first occurrence to be deleted :")))
        logger.info("Array after the removal of element is : ")
        logger.info(myArray)         
        
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[20,10,80,50,60,10,80,10,90,10])
        RemoveFirstOccurence(myArray)
    
    except Exception as err:
        logger.error(err)
