"""Write a function to compute and return the mode for the values contained in the given list.
"""

import statistics  
def get_mode():
    """To get mode from the given list"""

# creating the data set  
    data = [10, 20, 30, 30, 40, 40, 40, 50, 50, 60]  
  
# estimating the mode of the given set  
    Mode = statistics.mode(data) 

  # printing the estimated mode to the users    
    print("Mode of given set of data values is",Mode)  
 

get_mode()       