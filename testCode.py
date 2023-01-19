# 1. What roles do the parameters and the return statement play in a function definition?
"""Parameters play the role of describing what the function definition does as a definition. The return statment has """

# 2. Define a function named even. This function expects a number as an argument and returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A number is evenly divisible by 2 if the remainder is 0.)
def even(x):
    """X will return True if it equals 0 when divided, False otherwise"""
    if x % 2 == 0:
        return True
    else: 
        return False
print("Even? ", even(12))

# 3. Use the function even to simplify the definition of the function odd presented in this section.
def odd(x):
    """Returns true if even is false, Returns false if even is true"""
    if even is False:
        return True
    else: 
        return False
print("Odd? ", odd(10))

# 4. Define a function named summation. This function expects two numbers, named low and high, as arguments. The function computes and returns the sum of the numbers between low and high, inclusive.
def summation(low, high):
    """Computes the low and high numbers to a sum"""
    return low + high
print(summation(3,10))

# 5. What is the purpose of a main function?

# The purpose of the main function is to serve as an entry point into the script but has to be at the very end of the order of the script itself.