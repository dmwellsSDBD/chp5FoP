def absDiff(num1, num2):
    """Take in two numbers and returns the absolute value of the difference between the numbers"""
    diff = num1 - num2
    return abs(diff)


val1 = absDiff(35, 72)
val2 = absDiff(10, 4)
print("val1 = ", val1, "and val2 = ", val2)

print(val1, val2, absDiff(3, -2), 2 * absDiff(66, 77))

num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number:"))

print("The absoulte value of your difference is: ", absDiff(num1, num2))
