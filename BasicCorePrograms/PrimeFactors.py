'''
@Author: Naziya
@Date: 2021-07-08
@Last Modified by: Naziya
@Last Modified Time: 2021-07-08 03:10:00
@Title: Aim of the program is to print the prime factors of a input number.
'''


inputNumber = int(input("Enter the number for calculating the prime factors : "))
primeFactors = []
for i in range(2,inputNumber+ 1):
    if inputNumber % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            primeFactors.append(i)

print("Prime Factors are :",primeFactors)