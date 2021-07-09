'''
@Author: Naziya
@Date: 2021-10-08
@Last Modified by: Naziya
@Last Modified Time: 2021-10-08 00:1:00
@Title: Aim of the program is to find triplets whose sum is zero.
'''

def findTriplets(array,n):
    """
    Description:
        This function is used to find the triplets whosesum is zero
    Parameters:
        array is parameter which is the array list of elements.
        n is the length of the array.   
    """

    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (array[i]+array[j]+array[k] == 0):
                    return(array[i],array[j],array[k])
                
    if not found:
        return("Triplets not found")

if __name__ == "__main__":
    try:
        elements = int(input("Enter number of elements: "))
        array = []
        print("Enter the array elements")
        for i in range(elements):
            array.append(int(input()))

        # calling function    
        print(findTriplets(array,elements))

    except Exception as err:
        print("Enter a valid integer input",err)        