"""Write a function to do the following:
Take a list containing temperatures in fahrenheit
The function should return a list containing the temperature in Celsius.
"""

def get_celsius(fahren_list):
    """To find celsius from the list of fahrenheit"""
    celsius_list = []
    for f in fahren_list:
        c = 5 / 9 *(f - 32)
        celsius_list.append(c)
    return celsius_list

#Obtain the celsius and print the list
Celsius = get_celsius([32,45.2,67])
print("The celsius list :",Celsius)

