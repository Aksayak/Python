"""Write a function to compute and return the arithmetic mean for the values contained in the given list.
"""

def get_arithmeticmean(data):
    """To find arithmetic mean from the given values.
    """

    Arithmetic_mean = sum(data) / len(data)
    
    return Arithmetic_mean

#test the function 

#print Arithmetic mean
Arithmeticmean = get_arithmeticmean([2, 3, 4, 5, 6])
print(Arithmeticmean)


    