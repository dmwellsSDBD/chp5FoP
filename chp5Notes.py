# this is our Chapter 5 FoP Starting File
'''
Examples of lists

[1973, 1984, 2013, 2005]
["apples", "bananas", "oranges"]
[]  # this is an empty list
List of Lists
[[5, 9], [3,6,4], [3,9,10]]
'''
# variables in a list will print the variable value
# import math
# x = 2
# aList = [x, math.sqrt(x)]
# print(aList)

# list function
first = [1, 2, 3, 4]
second = list(range(1, 5)) #list function to create lists

print(first)
print(second)

# list are iterable using LOOPS
third = list("Hi there!")
print(third)

# measure the length of lists using len() function
print(len(first))

# first element in the second variable
print(second[0])

# Slicing Lists
print(first[2:4])

# Check for ==
print(first == second)

# Concatenate to a list
first = first + [5, 6]

# Check for ==
print(first == second)
print(first)

print()
print()

# print() function strips quotation marks from a string
# BUT it does not alter the look of a list
print("1234")
print([1, 2, 3, 4])
print()

# to print the list without brackets or commas, use a for loop
for number in [1,2,3,4]:
    print(number, end=" ")
    
print()
print()
# Check your list for values
students = ["Hayden", "Calvin", "Brendan", "Ryan", "Kaulin"]
if "Brendan" in students:
    print("Yes he is")
else:
    print("Nope, he is a loser")