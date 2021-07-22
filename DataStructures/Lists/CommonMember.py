'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to check if they have atleast one common member
'''

from LoggerFormat import logger

def commonMember():
    """
    Description:
        This function is used to check if they have atleast one common member
    """
    try:
        list1 = [1,2,3,4,5,6]
        list2 = [9,8,4,9,15,8]
        result = False
        for val1 in list1:
            for val2 in list2:
                if val1== val2:
                    result = True           
        print(result)
    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    commonMember()