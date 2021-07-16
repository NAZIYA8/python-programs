'''
@Author: Naziya
@Date: 14-07-2021
@Last Modified by: Naziya
@Last Modified Time: 14-07-2021
@Title: Program on Deck Of Cards 
'''

import deck

def deck_run():
    """
    Description: 
        This function is used to display the options to the user 
        objects to list.
    Pararmeter:
        self is an instance of the object.
    """

    d = deck.Deck()  # Build a deck
    print("Options :")
    print("1. Show Deck\n2. Shuffle Deck\n3. Deal 9 Cards to 4 players\n4. Show Player cards\n5. Exit\n")
    while True:
        while True:  # Take User Input
            try:
                user_choice = int(input("Enter choice (1-5) : "))
            except ValueError:
                print("Please Enter Integer Values from 1 to 5 only!")
            else:
                break
        if user_choice == 1:
            d.show()  # Show cards in deck
        elif user_choice == 2:
            d.shuffle()  # Shuffle cards in deck
        elif user_choice == 3:
            x = d.deal_to_players()  # Deal 9 cards to 4 players
        elif user_choice == 4:
            count = 1
            for player in x:
                print("-----------Player",count,"'s Cards-----------")
                for card in player:  # Display cards of each of the 4 players
                    print(card)
                count += 1
        else:
            break

# Driver Code
    deck_run()