'''
@Author: Naziya
@Date: 2021-10-08
@Last Modified by: Naziya
@Last Modified Time: 2021-10-08 00:35:00
@Title: Aim of the program is to print function to print two dimensional array.
'''

def twoDimensionalArray():
    """
    Description:
        This function is used to print a two dimensional array.
        It takes number of rows and columns and then also 
        the entries as input.
    """

    try:

        rows = int(input("Enter the number of rows: "))
        columns =int(input ("Enter the number of columns: "))

        # To store 2D array
        matrix= []
        print("Enter the entries row wise: ")

        for i in range(rows):
            array = []
            for j in range(columns):
                array.append(input())
            matrix.append(array)

        print("The 2D array is given: ")
        for i in range(rows):
            for j in range(columns):
                print(matrix[i][j],end=" ")
            print()

    except Exception as err:
        print("Enter numbers only:,err")

# function call
twoDimensionalArray()

        



