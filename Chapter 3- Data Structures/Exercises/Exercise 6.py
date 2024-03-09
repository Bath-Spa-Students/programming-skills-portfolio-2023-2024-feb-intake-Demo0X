#Defining old list
names = ["Dr. Zakir Naik", "Sheikh Mufti Menk", "Sheikh Mohammed Hoblos","Akhi Ayman"]

#removing names from the list until only 2 remain using pop()
for x in range(len(names)):
    if len(names) == 2:
        break
    else:
        print(f"We are sorry to inform you {names[x]} that we can not invite you to dinner")
        names.pop(x)
        print(f"Dear {names[x]} you are still invited to dinner at my house for Eid.")

#using del() function to erase my list
del names[:]

#printing the list
print(names)