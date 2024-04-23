#Vending Machine

# The first display menu that the vending machine shows with products and their codes
def start_menu():
    print("""
        Hello and Welcome to our Vending Machine!
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    print("""
        These are our items available right now: 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          <~Snacks~>
          ------------------------------
          >> Doritos    AED 6   Code: S1
          >> Nuts       AED 3   Code: S2
          >> Cheetos    AED 7.5 Code: S3
          >> Popcorn    AED 8   Code: S4
          ------------------------------

          <~Beverages~>
          ------------------------------
          >> Cola      AED 3.75 Code: B1
          >> Sprite    AED 2.5  Code: B2
          >> Pepsi     AED 2.75 Code: B3
          >> Juice     AED 3    Code: B4
          ------------------------------

          {Exit Code: X}
          """)


# The entire mechanism of the vending machine in this function
def machineworkings():
    # Dictionary with each items prices in numbers via their code
    codes = {
        "S1": 6,
        "S2": 3,
        "S3": 7.5,
        "S4": 8,
        "B1": 3.75,
        "B2": 2.5,
        "B3": 2.75,
        "B4": 3,
        "X": 0
        }
    print("""
          ------------------------------------------------------------------
          """)
    usrbudget = float(input("How much money will you be entering? "))
    snackstock = 100
    beveragestock = 100
    prices = []
    # For loop to iterate over the codes dictionary to add its values inside prices
    for x in codes.values():
        prices.append(x)
    # While loop for the user interface containing all the main mechanisms
    while True:
        # Stock checker 
        if snackstock <= 0 or beveragestock <= 0:
            print(""" We are out of stock. Restarting...""")
            start_menu()
            machineworkings()
        elif snackstock and beveragestock > 0:
            print("""
        <------------------------------------------------------------->
                  
            Sufficient Stock For Snacks and Beverages
                  
        <------------------------------------------------------------->
                  """)
        # User input for item codes
        usrcode = input("Please select your desired product by their code here: ")
        if usrcode.upper() in codes.keys():
                # If usrcode is correct and its above the items price then calculations take place as shown
                if usrcode.upper() == "S1" and usrbudget >= prices[0]:
                    change = usrbudget - prices[0]
                    print("You have successfully purchased Doritos!")
                    print(f"Here's your change: {change} AED")
                    # User budget will become the change calculated
                    usrbudget = change
                    #Snackstocks is subtracted for snack items  
                    snackstock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "S2" and usrbudget >= prices[1]:
                    change = usrbudget - prices[1]
                    print("You have successfully purchased Nuts!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    snackstock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "S3" and usrbudget >= prices[2]:
                    change = usrbudget - prices[2]
                    print("You have successfully purchased Cheetos!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    snackstock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "S4" and usrbudget >= prices[3]:
                    change = usrbudget - prices[3]
                    print("You have successfully purchased Popcorn!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    snackstock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "B1" and usrbudget >= prices[4]:
                    change = usrbudget - prices[4]
                    print("You have successfully purchased Cola!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    beveragestock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "B2" and usrbudget >= prices[5]:
                    change = usrbudget - prices[5]
                    print("You have successfully purchased Sprite!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    beveragestock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "B3" and usrbudget >= prices[6]:
                    change = usrbudget - prices[6]
                    print("You have successfully purchased Pepsi!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    beveragestock -= 10
# ------------------------------------------------------------------------------------
                elif usrcode.upper() == "B4" and usrbudget >= prices[7]:
                    change = usrbudget - prices[7]
                    print("You have successfully purchased Juice!")
                    print(f"Here's your change: {change} AED")
                    usrbudget = change
                    beveragestock -= 10
# ------------------------------------------------------------------------------------
                # If user enters X, which is the code for exit the system is shut down
                elif usrcode.upper() == "X":
                    print("""
                <..............................................................>
                 ______________________________________________________________  

                          
                Thank you for using our Machine. We hope to see you again soon!
                          
                 ______________________________________________________________
                <..............................................................>""")
                    break
                else:
                    print("Insufficient Funds.")
                    return machineworkings()
        else:
            print("Try Again. Example Use:'S1' ")


start_menu()
machineworkings()
