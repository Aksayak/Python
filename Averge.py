"""Create a module named average with the following functionality:
A function that computes the average of numerical values in the list
Code to seek user input of 4 values and call the above function and print the average computed. 
Use for loop and append method of list class. 
( use range() function to iterate a fixed number of times )
"""

def get_averge(list):
    """To get Averge"""
    a = sum(list) / len(list)
    return a

def get_input():
    """To get user input within range"""
    list_1 = []
    for num in range(4):
        list_1.append(eval(input("enter the ele")))
    return list_1

#Test the function
#Obtain the function and print it
Averge = get_input()
print(get_averge(Averge))
