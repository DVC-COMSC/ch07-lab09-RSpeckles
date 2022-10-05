# ******************************
# Make your Code
# ******************************
userInputs = input("Enter some names: ")

names = list(userInputs.split())

shortest = names[0]
longest = names[0]

for i in range(1, len(names)):
    if len(names[i]) < len(shortest):
        shortest = names[i]
    elif len(names[i]) > len(longest):
        longest = names[i]
    elif len(names[i]) == len(shortest):
        shortest = min(names[i], shortest)
    elif len(names[i]) == len(longest):  
        longest = min(names[i], longest)

print(shortest, longest)
