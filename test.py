

from Geometry.Circle import get_circle_area
radius =eval(input("enter the radius"))
print(get_circle_area(radius))

from Geometry.Circle import get_circle_circum
radius = eval(input("enter radius:"))
print(get_circle_circum(radius))

from Geometry.Rectangle import get_rect_area
length = eval(input("enter length:"))
breadth = eval(input("enter breadth:"))
print(get_rect_area(length,breadth))

from Geometry.Rectangle import get_rect_circum
length = eval(input("enter length:"))
breadth = eval(input("enter breadth:"))
print(get_rect_circum(length,breadth))

#Testing the get_area function


def test_input(value):
    try:
        value = float(value)
        return True
    except ValueError:
        return False

if test_input(radius) == True:
    radius = input(radius)
    area = get_circle_area(radius)
    circum = get_circle_circum(radius)
    print("The calculated value of area = ", area)
    print("The calculated value of circum",circum)
else:
    print("The Value Entered is not NUMERICAL. Enter a valid NUMERICAL.")


def test_input(value,value_1):
    try:
        value = float(value)
        value_1 = float(value_1)
        return True
    except ValueError:
        return False
    
#Testing the get_area function

if test_input(length,breadth) == True:
    length = input(length)
    breadth = input(breadth)
    area = get_rect_area(length,breadth)
    circum = get_rect_circum(length,breadth)
    print("The calculated value of area = ", area)
    print("The calculated value of circum",circum)
else:
    print("The Value Entered is not NUMERICAL. Enter a valid NUMERICAL.")