'''
@Author: Naziya
@Date: 13-07-2012
@Last Modified by: Naziya
@Last Modified Time: 13-07-2012
@Title: Aim of the program is AddressBook Problem using oops concept

'''


import json
from logging import ERROR, exception
from LoggerFormat import logger

class AddressBook:

    def __init__(self, file=None):
        self.file = file
        self.data = None

    def open(self):
        """
        Description: 
            This function is used to open the address book and store the data.
        Pararmeter:
            self is an instance of the object
        """

        try:
            with open(self.file) as f:
                self.data = json.load(f)
        except Exception as err:
            logger.error(err)

    def add_person(self):
        """
        Description: 
            This function is used to add person to the address book .
        Pararmeter:
            self is an instance of the object
        """ 
        while True:
            try:
                user_fname = input("Please enter First Name :\n")
                user_lname = input("Please Enter Last Name :\n")
                user_address = input("Please Enter Address :\n")
                user_city = input("Please Enter City :\n")
                user_state = input("Please Enter State :\n")
                user_zip = int(input("Please Enter Zip Code :\n"))
                user_phone = int(input("Please Enter Phone Number :\n"))
            except Exception as err:
                logger.error(err)
            else:
                break
    
        user_data = dict()  # Creating a dictionary to keep details of new entry
        user_data['fname'] = user_fname
        user_data['lname'] = user_lname
        user_data['address'] = user_address
        user_data['city'] = user_city
        user_data['state'] = user_state
        user_data['zip'] = user_zip
        user_data['phone'] = user_phone
        self.data['addressbook'].append(user_data)  # Adding dictionary to data


    def edit_person(self):
        """
        Description: 
            This function is used for updating or editing the user details.
        Pararmeter:
            self is an instance of the object
        """  
        logger.info("-------EDIT--------")
        try:
            user_fname = input("\nEnter First Name of User who's entry you would like to update :\n")
            user_lname = input("\nEnter Last Name of User who's entry you would like to update :\n")
            if self.search_entries(user_fname, user_lname) is True:  # Check if person exists in AddressBook
                for item in self.data['addressbook']:
                    # Checking for if both first name and last name point to the same item
                    if (user_fname == item['fname']) and (user_lname == item['lname']):
                        logger.info('What Parameter would you like to update? \n')
                        logger.info("1. Address\n2. City\n3. State\n4. Zip\n5. Phone\n")
                        user_choice = int(input("Please choose number 1-5 to update : \t"))
                        if user_choice in range(1, 5):
                            user_addr = input("\nPlease Updated Enter Address :")
                            user_city = input("\nPlease Updated Enter City : ")
                            user_state = input("\nPlease Updated Enter State : ")
                            user_zip = int(input("\nEnter Updated Zip Code :"))
                            # Re-assigning Values to self.data as we are editing
                            item['address'], item['city'], item['state'] = user_addr, user_city, user_state
                            item['zip'] = user_zip
                        elif user_choice == 5:
                            user_phone = int(input("Please Enter Updated Phone Number :"))
                            item['phone'] = user_phone
                        elif user_choice == 6:
                            break
                        else:
                            logger.info('Enter Valid Option')
            else:
                logger.info("ENTRY NOT FOUND!!")  # Entry not found if self.search_entry = False
        except Exception as err:
            logger.error(err)


    def delete_entry(self):
        """
        Description: 
            This function is used for deleting the user details.
        Pararmeter:
            self is an instance of the object
        """    
        logger.info("------Delete-------")
        try:
            user_fname = input("Enter First Name of Entry you would like to Delete :")
            user_lname = input("Enter Last Name of Entry you would like to Delete :")
            count = 0
            if self.search_entries(user_fname, user_lname) is True:  # Delete possible only when Person exists in AddBook
                for item in self.data['addressbook']:
                    # First name and Last need to point to same person
                    if (user_lname == item['lname']) and (user_fname == item['fname']):
                        del (self.data['addressbook'][count])
                    else:
                        count += 1
            else:
                logger.info("ENTRY NOT FOUND!!")  # If person does not exist in AddressBook entries
        except Exception as err:
            logger.error(err)

    def display_entries(self):
        """
        Description: 
            This function is used to display the entries in addressbook.
        Pararmeter:
            self is an instance of the object
        """
        logger.info("\n\tEntries\n")
        for item in self.data['addressbook']:
            print("Name :",item['fname'],item['lname'])
            print("Address :",item['address'],"\nCity :",item['city'],"\nState : ",item['state'])
            print("Zip :",item['zip'],"\nPhone :",item['phone'])
            print("\n")

    def search_entries(self, user_fname, user_lname):
        """
        Description: 
            This function is used to search if person exists in AddressBook.
        Pararmeter:
            self is an instance of the object
            user_fname is the user's first name
            user_lname is the user's last name
        """ 
        logger.info("-----Search--------")
        for entry in self.data['addressbook']:
            if user_fname == entry['fname'] and user_lname == entry['lname']:
                return True
        return False

    def save(self):
        """
        Description: 
            This function is used to Save the Address Book back into json file.
            self is an instance of the object
        """  
        try:
            with open(self.file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except exception as err:
            logger.error(err)
