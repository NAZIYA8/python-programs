'''
@Author: Naziya
@Date: 15-07-2021
@Last Modified by: Naziya
@Last Modified Time: 16-07-2021
@Title: Program on Commercial Data Processing.
'''

import stockaccount


def drive_account():
    """
    Description: 
        This function is used to carry out the operations like buy, sell,
        save and printing the report.
    """

    stock_account = stockaccount.StockAccount("./stockportfolio.json") # Initialize Stock portfolio
    print("Welcome to your Stock Portfolio \n")
    print("1. Buy Shares\n2. Sell Shares\n3. Save Transaction\n4. Print Report\n5. Exit\n")
    while True:
        user_choice = int(input("Please choose from above options. Enter 1-5 :\n"))
        if user_choice not in range(1, 6):
            raise ValueError("Enter Numbers between 1-5 only!")  
        else:
            if user_choice == 1:
                stock_account.buy()
                print(stock_account.get_transaction_time())
            elif user_choice == 2:
                stock_account.sell()
                print(stock_account.get_transaction_time())
            elif user_choice == 3:
                stock_account.save_file()
            elif user_choice == 4:
                stock_account.print_report()
            else:
                break


if __name__ == '__main__':
    drive_account()