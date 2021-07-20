'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to get string count
'''

from LoggerFormat import logger

def removeDuplicates():
    """
    Description:
        This function is used to remove duplicates from list. 
    """
    try:
        list1 = [2, 5, 1, 2, 2, 4, 2, 3, 4, 1]
        list2 = []
        for element in list1:
            if list2.__contains__(element):
                continue
            else:      
                list2.append(element)
        logger.info(" List after removing duplicate values: ")
        logger.info(list2)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    removeDuplicates()