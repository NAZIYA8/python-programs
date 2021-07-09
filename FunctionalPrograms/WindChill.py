'''
@Author: Naziya
@Date: 2021-10-08
@Last Modified by: Naziya
@Last Modified Time: 2021-10-08 00:2:00
@Title: Aim of the program is to calculate the wind chill.
'''
import math 

def windChill():
    """
    Description:
        This function is used to calculate the wind chill.
        It takes temperature and wind speed as input from the user and
        calculates wind chill.   
    """

    try:
        temperature = float(input("Enter temperature between 0 and 50 : "))
        windSpeed = float(input("Enter wind speed between 3 and 120 : "))

        if(temperature > 50 or windSpeed >120 or windSpeed < 3):
            print("Invalid!! Temperature should be between 0 and 50 and wind speed between 3 and 120")
        else:
            windChill = 35.74 + 0.62158 * temperature + (0.4275 * temperature - 35.75) * math.pow(windSpeed, 0.16)
            print("The Wind Chill is:",windChill,"deg F")

    except Exception as err:
        print("Root Cause of Exception is:",err)

# calling function
windChill()
