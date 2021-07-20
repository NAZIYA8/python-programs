'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to get string count
'''

from LoggerFormat import logger

def countString():
    """
    Description:
        This function is used to get string count 
        checking if the string length is 2 or more than 2
        checking if first and last character are same
        counting and printing the elements which satisfy these conditions
    """

    stringCount = 0
    string = ['abc', 'xyz', 'aba', '123']
    for elements in string:
        length = len(elements) 
        if length >= 2:
            if elements[0] == elements[-1]: 
                stringCount +=1
    logger.info("String count :")
    logger.info(stringCount)
                    
if __name__ == "__main__":
    countString()
