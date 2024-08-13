"""Extend the above function to also receive 2 additional optional arguments - 
   min and max to indicate the min and max values of the members of the list.
"""

import random
def get_minandmax(max_val,min_val,size):
    list_random = []
    if(max_val > 150):
        print("the max values are from above 150")
    elif(min_val <= 150 ):
        print("the mini values are from below or equals to 150")
    else:
        print("enter proper number")
              
    for num in range(size):
        n = random.randint(0,300)
        """Here we have taken range as min and max values."""
        list_random.append(n)
    return list_random

#Test and Obtain the function

Random = get_minandmax(0,300,10)
print(Random)

    
