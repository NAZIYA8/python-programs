'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to find difference between the two lists
'''

from LoggerFormat import logger

def difference():
    """
    Description:
        This function is used to find difference between the two lists
    """
    try:
        list1 = ['blue','green','white','black','red']
        list2 = ['red','white']
        list_difference = []
        for elements in list1:
            if elements not in list2:
                list_difference.append(elements)        
        logger.info("List difference :")
        logger.info(list_difference)
    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    difference()