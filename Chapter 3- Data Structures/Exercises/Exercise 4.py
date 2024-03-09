#People that will be invited to dinner

names = ["Imam Islam Sobhi", "Sheikh Mufti Menk", "Sheikh Mohammed Hoblos"]

#Invitation message with a for loop

for x in range(len(names)):
    print(f"Dear {names[x]}, I would like to invite you to dinner at my house for Eid")

print(f"Unfortunately one of our guests, {names[0]} will not be able to make it to the dinner.")