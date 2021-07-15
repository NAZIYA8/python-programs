'''
@Author: Naziya
@Date: 14-07-2021
@Last Modified by: Naziya
@Last Modified Time: 14-07-2021
@Title: Program on Deck Of Cards 
'''

import random

class Card: 

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  
        return f"{self.rank} of {self.suit}"


class Deck: 
    '''
    Description:
    To build deck of cards, shuffle deck and deal to players.
    Class variables suits and ranks as they do not change for instance of deck
    '''

    suits = ['Diamond', 'Club', 'Spade', 'Heart']
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    
   
    def __init__(self): 
        """
        Description: 
            This function is used to initialize the deck into list and add card 
            objects to list.
        Pararmeter:
            self is an instance of the object
        """
        
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):  
        """
        Description: 
            This function is used to Shuffle the deck using random.
        Pararmeter:
            self is an instance of the object
        """

        n = int(input("Enter number of times you would like to shuffle the deck"))
        for i in range(n):
            random.shuffle(self.deck)


    def deal(self):  
        """
        Description: 
            This function is used to deal card.
        Pararmeter:
            self is an instance of the object.
        Return:
            returns the card
        """
        return self.deck.pop()


    def show(self):  
        """
        Description: 
            This function is used to show the contents of the deck.
        Pararmeter:
            self is an instance of the object.
        """

        for card in self.deck:
            print(card)


    def deal_to_players(self):
        """
        Description: 
            This function is used to deal 9 cards to 4 players
            and return it.
        Pararmeter:
            self is an instance of the object.
        """

        players = []
        for i in range(4):
            player = []
            for j in range(9):
                player.append(self.deal())
            players.append(player)
        return players