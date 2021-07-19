'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to convert a list into a nested dictionary.
'''
from LoggerFormat import logger

def get_nested_dictionary():
    """
    Description:
        This function is used to convert a list into a nested dictionary..
    """
    try:

        list1 = ["abc", 'to', 'xyz'] 
        list2 = ['good', 'better', 'best'] 
        list3 = [2, 4, 6] 
    
        nestedDictionary = [{a: {b: c}} for (a, b, c) in zip(list1, list2, list3)] 
    
        logger.info("Nested dictionary :")
        logger.info(nestedDictionary)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    get_nested_dictionary()