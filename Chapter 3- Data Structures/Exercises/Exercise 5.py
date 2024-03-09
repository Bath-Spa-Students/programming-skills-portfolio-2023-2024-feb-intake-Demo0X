#Defining our old list

names = ["Imam Islam Sobhi", "Sheikh Mufti Menk", "Sheikh Mohammed Hoblos"]

#Replace first value
names[0] = "Dr. Zakir Naik"

#printing messages for each person in my new list
for x in range(len(names)):
    print(f"Dear {names[x]}, We are hosting a dinner party this Eid and would be honored if you could join us.")

print(f"Unfortunately due to some issue we will only be able to accomodate two people in the dinner party.")