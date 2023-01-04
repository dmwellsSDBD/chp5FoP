pets = ['dog', 'rat', 'frog', 'cat']
print(pets)

pets.sort()
print(pets)

pets.append('rabbit')
print(pets)

ratInd = pets.index('rat')
print('The rats position in the list is at index: ', ratInd)

pets.insert(0, 'bat')
print(pets)

pets.remove('cat')
print(pets)

pets.pop()
print(pets)



