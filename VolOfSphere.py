# Program Name: Volume of sphere
# Name: Josue Cifuentes
# Date: November 12, 2022
# Purpose of a Program: returns the volume of a sphere of radius r.

import math
r = int(input("What is the radius of your sphere?"))
def VolOfSphere():
     Volume = 4/3 * math.pi * r ** 3
     print("You're Volume is:", Volume)
VolOfSphere()