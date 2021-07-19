'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to count the items in a dictionary value
        that is a list.
'''

from LoggerFormat import logger

def countItems():
    """
    Description:
        This function is used to count the items in a dictionary value
        that is a list.
    """
    try:
        myDictionary = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'B' : 100,
            'C' : "Ok",
            'D' : [7, 0, 6, 2] }
        count = 0
        for value in myDictionary.items():
            if isinstance (value,list):
                count += len(value)
        logger.info(count)

    except Exception as e:
        logger.info(e)

if __name__ == "__main__":
    countItems()