#We don't have pi in python so we take it from the math module
import math


#Taking inputs
radius = int(input("Enter radius: "))

#Storing pi value
pi = math.pi

#Calculating Area
area = pi*(radius ** 2)
print(area)
