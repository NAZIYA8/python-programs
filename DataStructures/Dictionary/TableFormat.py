'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to print a dictionary in table format.
'''

from LoggerFormat import logger

def table_format():
    """
    Description:
        This function is used to print a dictionary in table format.
    """

    try:
        dict1 = {(0, 0): 'Berlin', (0, 1): 21, (0, 2): 'Male', 
                 (1, 0): 'Rachel', (1, 1): 20, (1, 2): 'Female', 
                 (2, 0): 'Samuel', (2, 1): 21, (2, 2): 'Male'
                } 
        print(" NAME ", " AGE ", "  GENDER " ) 
        for i in range(3): 
            for j in range(3): 
                print(dict1[(i, j)], end = '   ') 
            print()

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    table_format()
  
        