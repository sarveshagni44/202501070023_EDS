#Write a program that accepts the mass of an object (in kilograms) and its velocity (in meters per second),then calculates and displays the momentum of the object. The momentum is calculated using the formula:

#Input Format:

#A single floating-point number representing the mass of the object in kilograms.
#A single floating-point number representing the velocity of the object in meters per second.

#Output Format:

#The output will display calculated momentum with appropriate units (kgm/s) (rounded up to 2 decimal places).//

#code :

m=float(input())
v=float(input())
momentum=m*v
print(f"{momentum:.2f}kgm/s")
