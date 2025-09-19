import math

print("Rectangle:")
length=float(input("Enter the length:"))
width=float(input("Enter the width:"))
area_rectangle=length*width
perimeter_rectangle=2*(length+width)
print("Area of the rectangle:",area_rectangle)
print("Perimeter of the rectangle:",perimeter_rectangle)
print("\nCircle:")
radius=float(input("Enter the radius:"))
area_circle=math.pi*radius**2
print("Area of the circle:",area_circle)             
