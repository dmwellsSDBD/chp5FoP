lstA = ['frog', 'toad', 'salamander', 'newt']
lstB = lstA

lstB[2] = 'rabbit'
print("This list has changed:", lstB)
print("Unfortunately so has list A: ", lstA)


first = [20, 30, 40]
second = first
third = list(first)

print(first == second)
print(first == third)
print(first is third) # using the is operator