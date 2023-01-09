# [1, 3, 9 ,6, 7]


def average(lyst):
    theSum = 0
    for number in lyst:
        theSum += number
    return theSum / len(lyst)

listA = [1, 3, 9 ,6, 7]

varA = average(listA)

print(varA)

def printBackwards(text):
    """Takes a string, and prints it backwards"""
    backwdText = text[::-1]
    print("The text backwards is:", backwdText)
    
printBackwards("Hello Software")
printBackwards("A man, a plan, a canal: Panama!")

print('\n\n')
print("Boolean Functions")

def odd(x):
    """Returns True if x is odd or False otherwise."""
    if x % 2 == 1:
        return True
    else:
        return False


print(odd(57))

a = odd(94)
print(a)


