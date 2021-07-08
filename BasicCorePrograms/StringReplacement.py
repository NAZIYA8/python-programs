'''
@Author: Naziya
@Date: 2021-07-08
@Last Modified by: Naziya
@Last Modified Time: 2021-07-08 01:51:00
@Title: Aim of the program is to replace string from the message
with user input.
'''

import re
string = "Hello <<UserName>>, How are you?"
name = input("Enter a name with minimum 3 characters: ")
if not re.match("^[aA-zZ]{3,}$",name):
    print("Invalid!! Name should be of atleast 3 characters")
else:
    new_str = string.replace('<<UserName>>',name)
    print(new_str)