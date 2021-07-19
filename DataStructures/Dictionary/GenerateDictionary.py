'''
@Author: Naziya
@Date: 20-07-2021
@Last Modified by: Naziya
@Last Modified: 20-07-2021
@Title: Aim of the program is to generate a dictionary in a given form.
'''


def get_dictionary():
    """
    Description:
        This function is used to generate a dictionary.
    """
    number = int(input("Enter a number : "))
    print("Dictionary: ",{ variable : variable*variable for variable in range(1,(number+1))})

if __name__ == "__main__":
    get_dictionary()