#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Egg", "Chicken", "Cheese", "Grilled Cheese", "Ham", "Nutella","Pastrami", "Pastrami", "Pastrami"]
print("We have run out of Pastrami Sandwiches!")

finished_sandwiches = [""]

for x in range(len(sandwich_orders)):
    x = sandwich_orders.pop()
    print(f"I made your {x} sandwhich!")
    finished_sandwiches.append(x)
    if "Pastrami" in finished_sandwiches:
          finished_sandwiches.remove("Pastrami")

print("Here are the finished sandwiches: ")

for x in finished_sandwiches:
        print(x)