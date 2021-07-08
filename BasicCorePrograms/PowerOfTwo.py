'''
@Author: Naziya
@Date: 2021-07-08
@Last Modified by: Naziya
@Last Modified Time: 2021-07-08 03:05:00
@Title: Aim of the program is to take a input N and print power of 2
'''

def power_table(input):

    """
    Description:
        This function is used to input from the user and get the two power 
        of that number.It is also made sure that the input is between 0 and 31
        as two power 31 overflows as int.
    Parameter:
        input is used for getting user input.
    """

    for i in range(input+1):
        if i <= input:
            result = 2 ** i
    print("2 *", i, "is ", (result))


userinput = int(input("Enter the number N : "))
if(userinput >= 0 & userinput <= 31):
    power_table(userinput)
else:
    print("Invalid!!.Please enter a Valid Input ")