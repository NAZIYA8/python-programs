'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to count the values associated with the keys.
'''

from LoggerFormat import logger

def getValueCount():
    """
    Description:
        This function is used to count the values associated with the keys.
    """
    
    try:
        listItems =  [{'id': 1, 'success': True, 'name': 'Lary'}, 
                       {'id': 2, 'success': False, 'name': 'Rabi'}, 
                       {'id': 3, 'success': True, 'name': 'Alex'}]

        successCount = 0
        for dictionaryItems in listItems:
            if 'success' in dictionaryItems:
                if dictionaryItems['success'] == True:
                    successCount +=1
        logger.info("Success count as true is :")
        logger.info(successCount)

    except Exception as e:
        logger.info(e)

if __name__ == "__main__":
    getValueCount()