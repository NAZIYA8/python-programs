'''
@Author: Naziya
@Date: 23-07-2021
@Last Modified by: Naziya
@Last Modified: 23-07-2021
@Title: Aim of the program is to takes a list of words and returns the length of the longest
'''

from LoggerFormat import logger

def longestLength():
    """
    Description:
        This function is to takes a list of words and returns the length of the longest
    """

    try:
            wordList = ["one", "two", "third", "four"]
            finalList = []
            for word in wordList:
                finalList.append((len(word), word))
            finalList.sort() 
            print("The length of longest word is ",len(finalList[-1][1]))
    except Exception as err:
        print(err)

# Driver Code
longestLength()