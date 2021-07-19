'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is check multiple keys in dictionary.
'''

from LoggerFormat import logger

def multipleKeys():
    """
    Description:
        This function is used to check multiple keys in dictionary.
    """

    try:
        student = {'name': 'kinjal','class': 'B','roll_no': '2'}
        print(student.keys() >= {'class', 'name'})
        print(student.keys() >= {'name', 'kinjal'})
        print(student.keys() >= {'roll_no', 'name'})

    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    multipleKeys()