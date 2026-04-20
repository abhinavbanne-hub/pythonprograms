celsius_to_fahrenheit.py

def c_to_f(celsius):
    return (celsius * 9/5) + 32

fahrenheit_to_celsius.py

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_to_kelvin.py

def c_to_k(celsius):
    return celsius + 273.15

__init__.py

# This file makes the folder a package

🖥️ Main Program (main.py)

from temperature.celsius_to_fahrenheit import c_to_f
from temperature.fahrenheit_to_celsius import f_to_c
from temperature.celsius_to_kelvin import c_to_k

print("Temperature Conversion Menu")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", c_to_f(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", f_to_c(f))

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Kelvin:", c_to_k(c))

else:
    print("Invalid choice!")