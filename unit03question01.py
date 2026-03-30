# shapes.py
import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# main.py
import shapes

print("Choose shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = shapes.area_circle(r)
    print("Area of Circle:", area)

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = shapes.area_rectangle(l, w)
    print("Area of Rectangle:", area)

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = shapes.area_triangle(b, h)
    print("Area of Triangle:", area)

else:
    print("Invalid choice!")
