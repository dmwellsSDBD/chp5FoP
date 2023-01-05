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
    
print()
print()
example = [1,2,3,4]
example[3] = 10
print(example)

print()
print()

numbers = [2, 3, 4, 5]
for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2
    
print(numbers)

print()
print()

sentence = "This example has five words."
words = sentence.split()
print(words)

for index in range(len(words)):
    words[index] = words[index].upper()
    
print(words)


print("\n\n")
print("Searching Lists")

aList = [34, 45, 67, 82, 91]
target = 67 #int(input("Please enter a target number: "))

if target in aList:
    print("The number", target, "is located at index:", aList.index(target))
else:
    print(-1)
    
print("\n\n")
print("sorting Lists")

example = [5, 2, 7, 19, 45, 3, 24, 1]
print(example)

example.sort()
print(example)

print("\n\n")
print("Aliasing and Side Effects")
first = [10, 20, 30]
second = first
print("first list is: ", first)
print("second list is: ", second)

first[1] = 99
print("first list is: ", first)
print("second list is: ", second)

print("\n\n\n")
print("TUPLES----------------------------")

print("A Tuple is a linear, immutable collection")
print("Tuple Examples:")

fruits = ("apples", "banana")
meats = ("fish", "poultry")

food = meats + fruits
print(food)

veggies = ["celery", "beans"]
print(veggies, "is a list")

veggies = tuple(veggies)
print(veggies, "now it is a tuple")

badSingleton = (3)
print(badSingleton)

goodSingleton = (3,)
print(goodSingleton)