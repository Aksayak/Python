"""Write a function to find the selling price of the book when the list price and discount_percentage are given. 
Discount percentage should be optional. When no value is provided, the function will assume that the value is 10%
"""

def get_sellingprice(listed_price,discount_per):
    """Function to find sellingprice when listedprice and discount% are given. 
    Make discount = 10% when it is has no value.
    """

    if(discount_per == None):
        discount_per = 10
    else:
        SP = listed_price * (100 - discount_per) / 100
        return SP

#test for the get_sellingprice functions

#Obtain user input for LP
listed_price = eval(input("enter the value"))
discount_per = eval(input("enter the discount:"))

#Test for the function get_sellingprice
Selling_price = get_sellingprice(listed_price,discount_per)

#Print selling price
print(Selling_price)

