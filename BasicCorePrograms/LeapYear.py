'''
@Author: Naziya
@Date: 2021-07-08
@Last Modified by: Naziya
@Last Modified Time: 2021-07-08 02:40:00
@Title: Aim of the program is to print if the input year is a 
        leap year or not.
'''

import re

userInputyear = input("Enter a year to check if its leap or not: ")
if not re.match("^[0-9]{4}$",userInputyear):
    print("Year should be a 4 digit number")
userInputyear = int (userInputyear)
if (userInputyear)%4 == 0:
    if(userInputyear % 100) != 0 | (userInputyear % 400 == 0):
        print(userInputyear," is a Leap year")
    else:  
        print(userInputyear," is Not a Leap year")
else:
    print(userInputyear," is Not a Leap year")