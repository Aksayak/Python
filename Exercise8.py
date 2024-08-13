"""Write a function to do the following:
A list of distances in miles will be provided as an argument
The function should return a list containing the same values converted to Kilometers
"""

def get_kilos(miles_list):
    """To get kilometers from miles list"""
    kilo_list = []
    for mile in miles_list:
        kilo = 1.6 * mile
        kilo_list.append(kilo)
    return kilo_list

#Test the function
kilometer = get_kilos([1,2,5,4])
print("The kilometer list :",kilometer)
