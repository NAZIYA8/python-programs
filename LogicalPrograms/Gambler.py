'''
@Author: Naziya
@Date: 11-07-2021
@Last Modified by: Naziya
@Last Modified: 12-07-2021
@Title: Aim of the program is to simulate Gambler bet game and play until a condition is reached.
'''

import random

def start_gamble(stake, goal):
    """
    Description:
        This function is used to start gamble and get bet result
        Here a player start with stake and goal and plays the game
        until his pocket is empty or till he has achieved his goal.
    Parameters:
        stake is a starting amount of a player.
        goal is the target amount to win.
    """
    try:
        win = 0
        loss = 0
        totalGambles = 0

        while not(stake == 0 or stake == goal):
            gamble = random.randint(0, 1)
            totalGambles += 1
            if gamble == 0:
                stake += 1
                print("You Won the bet")
                win += 1

            else:
                stake -= 1
                print(" You lost the bet")
                loss += 1

        print(" You won ", win, " times ")
        print(" You Lost ", loss, " times ")
        print(" Your Total Gamble Played ", totalGambles, " times")

        winPercentage = float((win / totalGambles) * 100)
        print(" Win Percentage : ", winPercentage)
        lossPercentage = float((loss / totalGambles) * 100)
        print(" Loss Percentage : ", lossPercentage)

    except Exception as err:
        print("Root cause of error is :",err)

if __name__ == "__main__":

    print("..WELCOME..")

    try:
        stake = int(input("Enter the starting stake: "))
        while stake < 2:
            stake = int(input("Please start at least with 2$ : "))

        goal = int(input("Enter a winning goal amount: "))
        while goal < stake:
            goal = int(input("Enter amount greater than your stake:"))

    except Exception as err:
        print("Root cause of error is :",err)

start_gamble(stake, goal)