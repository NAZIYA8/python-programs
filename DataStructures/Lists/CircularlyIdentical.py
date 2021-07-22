'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to check whether two lists are circularly identical.
'''

from LoggerFormat import logger

def circularlyIdentical():
    """
    Description:
        This function is used to check whether two lists are circularly identical.
    """

    try:
        list1 = [10, 10, 0, 0, 10]
        list2 = [10, 10, 10, 0, 0]
        list1.extend(list1)
        result = False
        for i in range(len(list1)):
            if list2 == list1[i: i + len(list2)]:
                result = True
        logger.info(result)

    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    circularlyIdentical()


        