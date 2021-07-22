'''
@Author: Naziya
@Date: 22-07-2021
@Last Modified by: Naziya
@Last Modified: 22-07-2021
@Title: Aim of the program is to find list of words longer than n from a 
        given list of words
'''

from LoggerFormat import logger

def longerThanN():
    """
    Description:
        This function is used to find list of words longer than n
    """
    try:
            list_of_words = ['Apple', 'Banana', 'Pear', 'Pineapple', 'kiwi']
            longest_length = []
            word_length = int(input("Enter word length :"))
            for value in list_of_words:
                if len(value) > word_length:
                    longest_length.append(value)
            logger.info("Longest words are ")
            logger.info(longest_length)
    except Exception as err:
        logger.error(err)        
      
if __name__ == "__main__":
    longerThanN()