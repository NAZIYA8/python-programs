'''
@Author: Naziya
@Date: 2021-07-08
@Last Modified by: Naziya
@Last Modified Time: 2021-07-08 03:30:00
@Title: Aim of the program is to print the nth harmonic value.
'''

try:
    number = int(input("Enter A Number: "))
    assert number!=0
    harmonic=0
    for i in range(1,number+1):
        harmonic=harmonic+1/i
        print(harmonic)
except:
    print("Number Is Zero")