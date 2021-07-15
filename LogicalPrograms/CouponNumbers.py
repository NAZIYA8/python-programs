'''
@Author: Naziya
@Date: 11-07-2021
@Last Modified by: Naziya
@Last Modified: 11-07-2021
@Title: Aim of the program is to generate distinct coupon numbers.
'''

import random

class CouponNumber:
    @staticmethod
    def distinctCoupons():
        """
        Description: 
        This function is used to generating the distinct coupon numbers.
        Its takes number of coupons to generate from the user.
        """

        coupon = [] 
        randomNumbers=0 

        try:
            number = int(input("Enter The Number Of Coupons You Want To Generate: "))
            print("Distinct Coupon Numbers Generated")

            for element in range(number):
                couponNumber = random.randint(10,100)
                if couponNumber not in coupon:
                    coupon.append(couponNumber) 
                    print(couponNumber)
                    randomNumbers+=1
                else:
                    pass 
            print("Total Random Numbers Needed To Get All Distinct Numbers:",end = " ")
            print(randomNumbers,end = " ")

        except Exception as err:
            print("Not A Valid Number",err)

# Calling function 
CouponNumber.distinctCoupons() 