'''
@Author: Naziya
@Date: 11-07-2021
@Last Modified by: Naziya
@Last Modified: 11-07-2021

@Title: Aim of the program is to create a board game TicTacToe.
'''

import random


def player_marker():
    """
        Description: 
            This function is used to allow the player to choose the marker 
            between 'X' and 'O'.
            If user chooses 'X' then computer is assigned 'O' and viceversa.
        Return:
            Marker 'X' or 'O' for player and computer. 
    """

    while True:
        play_marker = input("Please choose 'X' or 'O' :\n")
        comp_marker = ''
        if play_marker.upper() == 'X':
            comp_marker = 'O'
            print("Player :" ,play_marker,"\nComputer :" ,comp_marker)
            return [play_marker.upper(),comp_marker]
        elif play_marker.upper() == 'O':
            comp_marker = 'X'
            print("Player :" ,play_marker,"\nComputer :" ,comp_marker)
            return [play_marker.upper(), comp_marker]
        else:
            print("Please choose 'X' or 'O' only!")


def display_board(board):
    """
        Description: 
            This function is used to display the board after each move.
        Parameter:
            board is the size of the board for creating the game board 
    """

    print("-------")
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|")
    print("-------")
    print("|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("-------")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|")
    print("-------")


def choose_position():
    """
        Description: 
            This function is used to allow the user to get the position 
            where he wants to put the marker.
        Return:
            position is returned when a valid position is input . 
    """

    while True:
        position = int(input("Please Enter position between 1-9 :\n"))
        if position in range(1,10):
            break
        else:
            print("Please enter Valid position")
    return position


def place_marker_player(player_marker,board):
    """
        Description: 
            This function is used to place the marker of the player 
            at a position which is input from the user
        Parameter:
            player_marker is the marker chosen by the player
            board is the size of the board for creating the game board
    """

    while True:
        pos = choose_position()
        if board[pos] == ' ':
            board[pos] = player_marker
            break
        else:
            print("Occupied!! Enter Position which is not taken")
            continue


def place_marker_computer(marker,board):
    """
        Description: 
            This function is used to place the marker of the computer 
        Parameter:
            marker is the marker assigned to the computer
            board is the size of the board for creating the game board
    """

    while True:
        pos = comp_position()
        if board[pos] == ' ':
            board[pos] = marker
            break


def comp_position():
    """
        Description: 
            This function is used to get the computer position randomly
            using the random function. 
    """

    comp_position = random.randint(1,9)
    return comp_position


def check_win(marker,board):
    """
        Description: 
            This function is used to check for the win 
        Parameter:
            marker is the marker of the user chosen.
            board is the current board taken to check.
    """

    #Check rows
    if (board[1]==board[2]==board[3] == marker) or (board[4]==board[5]==board[6]==marker) or (board[7] == board[8]==board[9] == marker):
        return True
    # Check columns
    elif (board[1]==board[4]==board[7] == marker) or (board[2]==board[5]==board[8]==marker) or (board[3] == board[6]==board[9] == marker):
        return True
    #Check Diagonals
    elif (board[1]==board[5]==board[9] == marker) or (board[3]==board[5]==board[7]==marker):
        return True
    return False


def full_board_check(board):
    """
        Description: 
            This function is used to check if the board is full 
        Parameter:
            board is current board taken to check if the positions are full or not
    """

    if ' ' in board:
        return False
    return True

global playing
playing = True


while playing:
    print("Welcome to Tic Tac Toe!! \n")
    print("Player chooses marker\n")
    board = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_marker,computer_marker = player_marker()
    x = random.randint(0, 1)
    if x == 1:
        print("Player",player_marker, "goes first \nComputer",computer_marker ," will go second")
        while True:
            display_board(board)
            print("Player's Turn\n")
            place_marker_player(player_marker,board)
            if check_win(player_marker,board):
                print("Player has won!!!!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break
            display_board(board)
            print("Computer's Turn\n")
            place_marker_computer(computer_marker,board)
            if check_win(computer_marker,board):
                print("Computer has Won!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break
    else:
        print("Computer",computer_marker,"goes first\nPlayer",player_marker, "will go second")
        while True:
            display_board(board)
            print("Computer's Turn\n")
            place_marker_computer(computer_marker,board)
            if check_win(computer_marker,board):
                print("Computer has won!!!!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break
            display_board(board)
            print("Player's Turn\n")
            place_marker_player(player_marker,board)
            if check_win(player_marker,board):
                print("Player has Won!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break

    display_board(board)
    break

   