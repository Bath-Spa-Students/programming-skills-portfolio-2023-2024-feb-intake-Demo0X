#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "IF_statement" : "Logical Conditions",
    "Variable" : "Containers for data values",
    "Lists" : "Used to tore multiple values in a variable",
    "Strings" : "arrays of bytes representing unicode characters",
    "Dictionaries" : "used to store data values in key:value pairs."

}

for x,y in glossary.items():
    print(f"{x}: {y}")

glossary["Data_Types"] = "numeric types (int, float, complex), string (str), boolean (bool), and collection types (list, tuple, dict, set)."
glossary["Comments"] = "Comments can be used to explain Python code."
glossary["Booleans"] = "Repsent two values 'True' or 'False'"
glossary["Operators"] = "used to perform operations on variables and values."
glossary["For_loops"] = "used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)."