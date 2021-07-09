'''
@Author: Naziya
@Date: 2021-10-08
@Last Modified by: Naziya
@Last Modified Time: 2021-10-08 01:40:00
@Title: Aim of the program is to find the euclidean distance from origin 
        to the point (x,y).
'''

import math

def euclideanDistance():
    """
    Description:
        This function is used to get the euclidean distance from origin 
        to the point (x,y).It takes x-point and y-point as input from the 
        user and calculates distance from origin.    
    """

    try:
        xPoint = int(input("Enter the number for x-point: "))
        yPoint = int(input("Enter the number for y-point: "))

        distance = math.sqrt((xPoint*xPoint + yPoint*yPoint))
        print("Euclidean distance is: ",distance)
    
    except Exception as err:
        print("Please Enter valid integer input",err)

# calling function
euclideanDistance()