# If then 3 example
# Author: Kat
# Date: 02/11/2022

# Scalene triangle: All sides have different lengths
# Isosceles triangle: two sides have the same length
# Equilateral triangle: All the sides are equal

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if a != b and b != c and a != c:
    print("This is a csaling triangle.")
elif a ==b and b == c and a == c:
    print("This is a equilateral triangle.")
else:
    print("This is an isosceles triangle.")
        
    
