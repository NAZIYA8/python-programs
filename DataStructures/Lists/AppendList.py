'''
@Author: Naziya
@Date: 21-07-2021
@Last Modified by: Naziya
@Last Modified: 21-07-2021
@Title: Aim of the program is to clone list
'''

from LoggerFormat import logger

def appendList():
    try:
        list1 = [1,2,[3,4],"list",67]
        list2 = [43,21,2,0,(3,4)]
        for elements in list2:
            list1.append(elements)
        logger.info("Resultant of first list and second list")    
        logger.info(list1)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    appendList()