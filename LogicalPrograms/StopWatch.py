'''
@Author: Naziya
@Date: 11-07-2021
@Last Modified by: Naziya
@Last Modified: 11-07-2021
@Title: Aim of the program is to simulate Stopwatch.
'''

import time

def stopWatch():
    """
        Description: 
            This function is used for measuring the time that elapses between
            the start and end clicks
    """

    try:
        startWatch = int(input("Enter To Start The Watch:"))
        endWatch = int(input("Enter To Stop The Watch:"))
        startWatch = time.time()
        endWatch = time.time()
        
        timeElapsed = endWatch - startWatch
        print("Time Elapsed in seconds = ",timeElapsed)

    except Exception as err:
        print("Root cause of error is :",err)    

# calling Function    
stopWatch()