"""Modify the above module to keep the size of the list of values flexible. 
Use a while loop to allow the user to enter any number of values.
"""

def get_averge(list):
    """To find Averge"""
    a = sum(list) / len(list)
    return a

def get_input():
    """To get flexible inputs"""
    list_1 = []
    while True:
        n = input("enter number")
        if n.lower() == "stop":
            break
        else:
            list_1.append(eval(input("enter the ele")))

    return list_1

#Test the function
Averge = get_input()
#Obtain the averge and print it
print(get_averge(Averge))

