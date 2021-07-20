'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to add member to a set
'''

from LoggerFormat import logger

def addMember():
    """
    Description:
        This function is used to add member to a set
    """

    try:
        mySet = {1, "pqr", 2 , 3, "ab", 2, 5}
        logger.info("Original Set")
        logger.info(mySet)
        logger.info("Set after adding members")
        mySet.add(10)
        mySet.add("ok")
        logger.info(mySet)

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    addMember()
