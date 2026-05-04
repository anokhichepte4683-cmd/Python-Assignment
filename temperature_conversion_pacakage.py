from my_module import celsius_to_fahrenheit
from my_module import fahrenheit_to_celsius
from my_module import celsius_to_kelvin
print("Temperature conversion choices ")
print("Choice 1) celsius to fahrenheit") 
print("Choice 2) fahrenheit to celsius")
print("choice 3) celsius to kelvin")
choice = int(input("Enter the number of your choice:"))
if choice == 1 :
    c = float(input("Enter celsius :"))
    print("Conversion :",celsius_to_fahrenheit.convert(c))
if choice ==2 :
    f = float(input("Enter value"))
    print("Conversion",fahrenheit_to_celsius.convert(f))
if choice ==3 :
    g = float(input("Enter celsius "))
    print("Conversion ",celsius_to_kelvin.convert(g))