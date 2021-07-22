'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to multiplies all the items in a list.
'''

from LoggerFormat import logger

def multiplyList():
    """
    Description:
        This function is used to multiplies all the items in a list.
    """
    try:
        list1 = [2,4,9,10]
        list2 = [1,5,14,2]
        multiplicationList = []
        for number1, number2 in zip(list1,list2):
            multiplicationList.append(number1*number2)
        logger.info("Product of list1 and list2 : ")
        logger.info(multiplicationList)
    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    multiplyList()