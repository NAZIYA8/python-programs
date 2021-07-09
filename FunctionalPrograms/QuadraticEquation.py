'''
@Author: Naziya
@Date: 2021-10-08
@Last Modified by: Naziya
@Last Modified Time: 2021-10-08 02:00:00
@Title: Aim of the program is to find the roots of the equation 
        ie. a*x*x + b*x + c = 0.
'''

import math 

def quadraticEquation():
    """
    Description:
        This function is used to find the roots of the equation by taking a, b, c 
        as input from the user.
        It calculates delta using the fomula an then the roots of the equation.    
    """

    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))

        delta = abs(b*b - 4*a*c)
        root1 = (-b + math.pow(delta, 1/2)) / (2*a)
        root2 = (-b - math.pow(delta, 1/2)) / (2*a)
        print("First root of the equation is : ",root1)
        print("Second root of the equation is : ",root2)

    except Exception as err:
        print("Root Cause of Exception is :",err)

# Calling function
quadraticEquation()        