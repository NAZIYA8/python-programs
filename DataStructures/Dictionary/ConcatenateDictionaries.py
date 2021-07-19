'''
@Author: Naziya
@Date: 19-07-2021
@Last Modified by: Naziya
@Last Modified: 19-07-2021
@Title: Aim of the program is to concatenate given dictionaries.
'''


from LoggerFormat import logger


def concatenate_dictionary():
    """
    Description:
        This function is used to concatenate the given 3 dictionaries.
    """

    try:
        dict1={1:10, 2:20}
        dict2={3:30, 4:40}
        dict3={5:50, 6:60}
        dict4={**dict1 , **dict2 , **dict3}  
        logger.info(" New dictionary after concatenating : ")
        logger.info(dict4)
    except Exception as err:
        logger.error(err)    	

if __name__ == "__main__":
    concatenate_dictionary()
