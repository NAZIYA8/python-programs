'''
@Author: Naziya
@Date: 13-07-2021
@Last Modified by: Naziya
@Last Modified Time: 14-07-2021
@Title: Aim of the program is AddressBook Problem using oops concept

'''

import addressbook
from LoggerFormat import logger


class AddBook:

    def main(self):

        address_book = addressbook.AddressBook("./addbook.json")  # Create Address Book obj
        address_book.open()  # Open Address Book
        logger.info("ADDRESS BOOK")
        logger.info
        ("1. Add New Entry\n2. Edit an Existing Entry\n3. Delete an Existing Entry"
              "\n4. Search for an Entry\n5. Display Entries\n6. Save\n7. Exit")
        while True:
            user_choice = int(input("\nPlease Select an action (1-7) : "))
            if user_choice == 1:
                address_book.add_person()
            elif user_choice == 2:
                address_book.edit_person()
            elif user_choice == 3:
                address_book.delete_entry()
            elif user_choice == 4:
                first = input("Enter First Name of Entry to Search")  # First name to search
                last = input("Enter Last Name of Entry to Search")  # Last name to search
                logger.info(address_book.search_entries(first, last))
            elif user_choice == 5:
                address_book.display_entries()
            elif user_choice == 6:
                address_book.save()
            else:
                break

# Driver Code for address book
if __name__ == '__main__':
    a=AddBook()
    a.main()
    