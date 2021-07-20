'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to get unique values in a dictionary.
'''

from LoggerFormat import logger

def uniqueValues():
    """
    Description:
        This function is used to get unique values in a dictionary.
    """

    try:
        logger.info("Original Dictionary")
        dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        logger.info(dict)
        logger.info("Unique Values are: ")
        unique = list(set(val for items in dict for val in items.values()))
        logger.info(unique)
        a= [val for items in dict for val in items.values()]
        print(type(a))
        print(a)
    except Exception as err:
        logger.error(err)

        
if __name__ == "__main__":
    uniqueValues()