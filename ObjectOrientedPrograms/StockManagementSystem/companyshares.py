'''
@Author: Naziya
@Date: 15-07-2021
@Last Modified by: Naziya
@Last Modified Time: 16-07-2021
@Title: Program on Commercial Data Processing.
'''

import json
import datetime


class CompanyShares:
    # Class variable data to store json file data
    with open("./companylisting.json", 'r') as f:
        data = json.load(f)

    def __init__(self, symbol=None, number_of_shares=None, price=None):
        self.symbol = symbol  # variable to take company name
        self.number_of_shares = number_of_shares  # Variable to take number of shares company has
        self.price = price  # variable for price of each share
        self.transaction_time = None

    def get_transaction_time(self):
        """
        Description: 
            This function is used to get transaction time when we buy or sell shares.
        Parameter:
            self is an instance of the object.
        Return :
            transaction time
        """
        self.transaction_time = datetime.datetime.now()
        return self.transaction_time

    def generate_company(self):
        """
        Description: 
            This function is used to generate a list of company objects.
        Parameter:
            self is an instance of the object.
        """
        
        listing = list()
        for item in self.data['company']:
            listing.append(CompanyShares(item['name'], item['numberofshares'], item['shareprice']))
        return listing

    @staticmethod
    def save(data_):
        """
        Description: 
            This function is used to Save data into json file.
        """
         
        with open("./companylisting.json", 'w') as f:
            json.dump(data_, f, indent=2) 