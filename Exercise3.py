"""Write a function to compute and return the median for the values contained in the given list. 
"""

def get_median(data):
    """Find the median."""

    data = sorted(data)
    if(len(data) % 2 == 0):
        a = len(data) // 2
        b = (len(data) // 2) - 1
        median = (data[a] + data[b]) / 2
        return median
    
    else:
        median = data / 2
        return median
    
 #Obtain Median
median = get_median([2,4,6,4,10,5,6,7])
print(median)





