'''
@Author: Naziya
@Date: 13-07-2021
@Last Modified by: Naziya
@Last Modified Time: 13-07-2021
@Title: Aim of the program is AddressBook Problem using oops concept.
'''


import json
from logging import ERROR, exception
from LoggerFormat import logger
from UserDetailsValidation import ValidateDetails

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
        user_data = dict() # Creating a dictionary to keep details of new entry

        user_fname = ValidateDetails.validateFirstName()
        user_data['user_fname'] = user_fname
        user_lname = ValidateDetails.validateLastName()
        user_data['user_lname'] = user_lname
        user_address = ValidateDetails.validateAddress()
        user_data['user_address'] = user_address
        user_city = ValidateDetails.validateCity()
        user_data['user_city'] = user_city
        user_state = ValidateDetails.validateState()
        user_data['user_state'] = user_state
        user_zip = ValidateDetails.validateZipcode()
        user_data['user_zip'] = user_zip
        user_phone = ValidateDetails.validateNumber()
        user_data['user_phone'] = user_phone
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
            print("First name and Last name of the user who's entry you would like to update:\n")
            user_fname = ValidateDetails.validateFirstName()
            user_lname = ValidateDetails.validateLastName()
            if self.search_entries(user_fname, user_lname) is True:  # Check if person exists in AddressBook
                for item in self.data['addressbook']:
                    # Checking for if both first name and last name point to the same item
                    if (user_fname == item['user_fname']) and (user_lname == item['user_lname']):
                        logger.info('What Parameter would you like to update? \n')
                        logger.info("1. Address\n2. City\n3. State\n4. Zip\n5. Phone\n")
                        user_choice = int(input("Please choose number 1-5 to update : \t"))
                        if user_choice in range(1, 5):
                            user_address = ValidateDetails.validateAddress()
                            user_city = ValidateDetails.validateCity()
                            user_state = ValidateDetails.validateState()
                            user_zip = ValidateDetails.validateZipcode()
                            # Re-assigning Values to self.data as we are editing
                            item['user_address'], item['user_city'], item['user_state'] = user_address, user_city, user_state
                            item['user_zip'] = user_zip
                        elif user_choice == 5:
                            user_phone = ValidateDetails.validateNumber()
                            item['user_phone'] = user_phone
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
            print("First name and Last name of the user who's entry you would like to delete: \n")
            user_fname = ValidateDetails.validateFirstName()
            user_lname = ValidateDetails.validateLastName()
            count = 0
            if self.search_entries(user_fname, user_lname) is True:  # Delete possible only when Person exists in AddBook
                for item in self.data['addressbook']:
                    # First name and Last need to point to same person
                    if (user_lname == item['user_lname']) and (user_fname == item['user_fname']):
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
            print("Name :",item['user_fname'],item['user_lname'])
            print("Address :",item['user_address'],"\nCity :",item['user_city'],"\nState : ",item['user_state'])
            print("Zip :",item['user_zip'],"\nPhone :",item['user_phone'])
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
            if user_fname == entry['user_fname'] and user_lname == entry['user_lname']:
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
