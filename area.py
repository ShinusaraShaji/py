area=lambda a:a*a
a=int(input("Enter side of square:"))
print("area of a square is",area(a))
area=lambda l,b:l*b
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("area of a rectangle is",area(l,b))
area=lambda b,h:(b*h)/2
b=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of a triangle:"))
print("the area of triangle is",area(b,h))
