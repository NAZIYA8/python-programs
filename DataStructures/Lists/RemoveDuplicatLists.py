'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is  remove duplicates from list of lists 
'''

from LoggerFormat import logger

def removeDuplicates():
    """
    Description:
        This function is used to remove duplicates from list of lists 
    """
    try:
        list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        new_list = []
        for elements in list1:
            if elements not in new_list:
                new_list.append(elements)
        logger.info("New list without duplicates")        
        logger.info(new_list)
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    removeDuplicates()