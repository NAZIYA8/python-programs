'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to display formatted text (width=50) as output.
'''

from LoggerFormat import logger

def formattedText():
    """
    Description:
        This function is to display formatted text (width=50) as output.
    """
    try:
        string1 = "width"
        logger.info("{}={}".format(string1, 50))
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":
    formattedText()










