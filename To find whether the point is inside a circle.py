R=eval(input("Enter the radius: "))
A_C=eval(input("Enter the abscissa of the centre of a circle: "))
O_C=eval(input("Enter the ordinate of the centre of circle: "))
A_P=eval(input("Enter the abscissa of a point: "))
O_P=eval(input("Enter the ordinate of a point: "))
Distance= (((A_P-A_C)**2)+((O_P-O_C)**2))**(1/2)
if Distance<R:
    print("Point is inside a circle")
elif Distance==R:
    print("Point lies on the circumference")
else:
    print("Point is outside the circle")