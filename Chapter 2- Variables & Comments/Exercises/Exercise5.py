#The persons balance
balance = 50

#Price of USB
usb_price = 6

#Number of USBs she can get -->
number = 50//6
#Amount she has left
amount = balance - (number * usb_price) 
print("She bought " + str(number) + " USBs and has " + str(amount) + " pounds left.")