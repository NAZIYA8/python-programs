'''
@Author: Naziya
@Date: 2021-07-08
@Last Modified by: Naziya
@Last Modified Time: 2021-07-08 02:15:00
@Title: Aim of the program is to flip a coin for input number of times and 
        find the percentage of Heads vs Tails
'''

import random


def flipCoin():
    """
    Description:
        This function is used to take input the number of times the user
        wants to flip a coin and check heads or tails.And later get the 
        percentage of heads vs Percentage of Tails.
    Parameter:
        input is used for get user input which gives number of times user
        wants to flip a coin.
    """

    numOfFlip = int(input("Enter the number of times you want to flip coin: "))
    tail = 0
    head = 0
    for toss in range(numOfFlip):
        toss = random.random()
        if toss < 0.5:
            tail+=1
        else:
            head+=1
        percentHead = (head/numOfFlip)*100
        percentTail = 100 - percentHead
    print("Percentage of Head:",percentHead)
    print("Percentage of Tail:",percentTail)

flipCoin()