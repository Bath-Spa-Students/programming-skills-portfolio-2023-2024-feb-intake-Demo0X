#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, text):
    return print(f"The size of this shirt is {size} and it will have {text} written on it!")

make_shirt("Large", "Coder")