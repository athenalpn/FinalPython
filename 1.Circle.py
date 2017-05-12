
"""Program requests a radius value from the user then calculate and print out the 
diameter, circumference, and area of a circle with that radius. Uses the math module to import the value of π.

User, input a value for the radius and program will give you back values for diameter, circumference and area of a circle
"""

from math import pi


print("Enter a radius")
radius = input()
radius = float( radius )

area = pi * radius * radius
circ = 2 * pi * radius
diam = radius * radius

print("Area of Circle is", area )
print ("Circumference of Circle is", circ)
print("Diameter of Circle is:", diam)

