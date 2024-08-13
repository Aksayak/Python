"""Write a function to return a list of even numbers. The size of the list is to be given as an argument to the function.
"""

def get_even(size):
    """To get list of even numbers"""
    list_of_even = []
    for num in list:
        if num % 2 == 0:
            list_of_even.append(num)
        else:
            continue
    return list_of_even

# Take input of all the elements as a string 
s = input("Enter the elements: ")


# Use map function to wrap-up them and converting to desired data type.
list = [eval((num)) for num in s.split()]
Even = get_even(7)

print(Even)
