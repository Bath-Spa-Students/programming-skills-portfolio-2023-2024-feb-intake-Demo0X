#Defining a list
locations = ["Great Wall of China", "London Bridge", "Tokyo Tower", "Pyramid of Giza", "Grand Canyon"]
print(locations)

#printing with sorted()
print(sorted(locations))
print(locations)

#reversing list with sorted()
print(sorted(locations, reverse=True))
print(locations)

#reversing the list
locations.reverse()
print(locations)

#reversing the list again to bring it back to original form
locations.reverse()
print(locations)

#sorting list in alphabetical order
locations.sort()
print(locations)

#sorting the list in reverse alphabetical order 
locations.sort(reverse=True)
print(locations)
