"""
Python Dictionaries:
     {Key : Values}
     A phone book: {"Savannah":"476-3321", "Wade":"351-7743"}
"""


ages = dict()

# Adding new entries to a dictionary: 
ages['Marek'] = 37
ages['Michaela'] = 23
ages['Imani'] = 12
print(ages)

# Updating an entry:
print("Imani has a birthday!")
# ages['Imani'] = ages["Imani"] + 1
# print("She is now", ages['Imani'], 'years old.')

# # Calculate an age
# yearOfBirth = {"Wade": 2004, 'Mackenzie': 2005, "Wells": 1973}

# x = yearOfBirth['Wells']
# currentYear = 2023
# age = currentYear - x
# print("At some point this year, this person will turn", age)

"""
Adding Keys and Replacing Values
"""
info = {} # created empty dictionary
info["name"] = "Sandy" # added key and value
info["occupation"] = "hacker"
print(info)

info["occupation"] = "manager"
print(info)