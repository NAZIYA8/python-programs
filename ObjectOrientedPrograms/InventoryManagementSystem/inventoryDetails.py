'''
@Author: Naziya
@Date: 14-07-2012
@Last Modified by: Naziya
@Last Modified Time: 14-07-2012
@Title: Aim of the program is AddressBook Problem using oops concept

'''

import json
from LoggerFormat import logger


class Inventory:

    def __init__(self):
        pass

    def invertory_details(self):
        """
        Description: 
            This function is used where the data is loaded and inventory values 
            are calculated and then dumped back as a json string.
        Pararmeter:
            self is an instance of the object
        """

        try:
            with open("./inventory.json","r") as file:    #reading the json file
                data = json.load(file)
        except Exception as err:
            logger.error("Unable To Open The File:",err)


        rice_list=data['rice']
        for val1 in range(len(rice_list)):
            rice = rice_list[val1].get("weight") * rice_list[val1].get("price_per_kg")

        pulses_list=data['pulses']        
        for val2 in range(len(pulses_list)):
            pulses = pulses_list[val2].get("weight") * pulses_list[val2].get("price_per_kg")

        wheat_list=data['wheat']
        for val3 in range(len(wheat_list)):
            wheat = wheat_list[val3].get("weight") * wheat_list[val3].get("price_per_kg")

        logger.info("Total value of rice is:")
        logger.info(rice)
        logger.info("Total value of pulse is:")
        logger.info(pulses)
        logger.info("Total value of wheat is:")
        logger.info(wheat)    

        try:
            with open("./updated_inventory.json","w") as write_file:
                json.dump(data, write_file,indent=4)
        except Exception as err:
            logger.error("Unable To Write The File:", err)


if __name__ == "__main__": 
    inventory = Inventory()           
    inventory.invertory_details()            