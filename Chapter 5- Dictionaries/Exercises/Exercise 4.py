#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#* Use a loop to print the name of each river included in the dictionary.
#* Use a loop to print the name of each country included in the dictionary.
rivers = {
    "Yangtze" : "China", 
    "Amazon" : "Brazil", 
    "Mississippi" : "United States"
    }

#sentence for each river
for x,y in rivers.items():
    print(f"The {x} River runs through {y}")

#name of each river
for x in rivers.keys():
    print(x)

#country of each river
for x in rivers.values():
    print(x)