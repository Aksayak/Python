"""Write a function that returns a list of random integers. The length of list is to be provided as an argument
"""

import random
def get_random(limit_1,limit_2,size):
    """To get random number within the length of the list"""
    list_random = []
    for num in range(size):
        n = random.randint(limit_1,limit_2)
        list_random.append(n)
    return list_random

#Obtain the function and print it  
Random = get_random(0,30,10)
print(Random)
    
