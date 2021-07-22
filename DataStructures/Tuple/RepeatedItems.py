'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is find the repeated items of a tuple.
'''

from LoggerFormat import logger

def repeatedItems():
    """
    Description:
        This function is to find the repeated items of a tuple.
    """
    try:
        tuple1 = ("black",50, 70, "blue", "red ", 50,"Blue", "black" , 20, 10)
        repeat = []
        
        for element in range(tuple1.__len__()):
            for element2 in range(element + 1, tuple1.__len__()):
                if tuple1[element] == tuple1[element2] and (repeat.__contains__(tuple1[element2])) is False:
                    repeat.append(tuple1[element2])
        logger.info(" Repeated elements of a tuple are ")
        logger.info(repeat)
    except Exception as err:
        logger.info(err)
     
        
if __name__ == "__main__":
    repeatedItems()