"""The Pythagorean equation for a right triangle is a^2 + b^2 = c^2 , where c is the hypotenuse 
while a and b are the remaining sides. 
This program calculates all values for a right triangle.
Will print the values of Hypotenuse, Smaller angle, and last angle.
Uses math imported to have the ability geometry functions.

As the user, you will input two lengths of triangle sides, this will give you back the other values in the triangle.
"""
import math
hypot = 0
angle = 90
l = input('Input first length: ')
r = input('Input second length: ')
hypot = math.hypot(int(l), int(r))
a = math.cos(math.radians(angle))
smaller_angle = (math.sin(math.radians(angle)) * 5) / hypot
smaller_angle = math.asin(smaller_angle)
smaller_angle = math.degrees(smaller_angle)
langle = 180 - angle - smaller_angle
print('Hypotenuse: {:.2f}, Smaller Angle: {:.2f}, Last Angle: {:.2f}'.format(hypot, smaller_angle, langle))
