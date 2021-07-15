'''
@Author: Naziya
@Date: 14-07-2021
@Last Modified by: Naziya
@Last Modified Time: 14-07-2021
@Title: Program on Stock Management System to calculate the value of 
        stocks in each company and total value of stock portfolio.
'''

import json

class StockPortfolio:

    def __init__(self, file):  # Initialise instance variable for stockportfolio obj
        self.file = file
        self.stock_data = None
        try:
            with open(self.file, 'r') as f:
                self.stock_data = json.load(f)  # Set stock data from file
        except FileNotFoundError:
            print("File not found")

    def stock_calculations(self):
        """
    Description: 
        This function is used to calculate value of stocks in each company 
        and Total value of stock portfolio.
    Pararmeter:
        self is an instance of the object.
    """

        total = 0
        for item in self.stock_data["stock"]:
            print("\nStock Name :",item['stockname'],"\nNumberof Shares :",item['numberofshares'],
                  "\nPrice per Share:",item['shareprice'])
            print("Total Stock Value of",item['stockname'],item['numberofshares']*item['shareprice'])
            total += item['numberofshares']*item['shareprice']
        print("\nTotal Value of Stock Portfolio is :",total)


# Driver code for above Code
if __name__ == "__main__":
    stockport = StockPortfolio("./stockportfolio.json")
    stockport.stock_calculations()

