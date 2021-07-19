'''
@Author: Naziya
@Date: 19-07-2021
@Last Modified by: Naziya
@Last Modified: 19-07-2021
@Title: Aim of the program is to count the number of occurrence of element
        in array
'''

import array
from LoggerFormat import logger

def occurence(myArray):
    """
    Description:
        This function is used to find number of occurence of element in array
    Parameter:
        Myarray is for array elements.
       
    """
    count = 0
    try:
        number_count = myArray.count(int(input("Enter the number you want to count :")))
        logger.info("Number of occurance is : ")
        logger.info(number_count)         
        
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    try:
        myArray = array.array("i",[10,20,10,50,60,10,80,10,90,10])
        occurence(myArray)
    
    except Exception as err:
        logger.error(err)
