#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet

pets = [
    {"animal": "Panther", "owner" : "Tayyeb"},
    {"animal" : "Hound", "owner" : "Ali"},
    {"animal" : "Bird", "owner" : "Geoff"}
     ]

for x in pets:
    print(f"Animal: {x['animal']}")
    print(f"Owner: {x['owner']}")
