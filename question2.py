#write a program that calculates the volume of a cylinder
radius = int(input("enter the radius of a cylinder:"))
height = int(input("enter the height of a cylinder:"))
import math 
pievalue = math.pi 
volume = pievalue*radius**2*height
print(f'the volume of the cylinder with height {height} and radius {radius} is {volume:.2f}')
