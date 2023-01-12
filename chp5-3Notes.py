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


print("\n\n\n")
print("Accessing Values -----------------------------------")
print(info)

info["fullTime"] = True
print(info)

if "occupation" in info:
     sandysJob = info["occupation"]
else:
     print("Please add Occupation to information.")
     
if "fullTime" in info:
     status = info["fullTime"]
     if status == True:
          ftEmp = "is"
     else: 
          ftEmp = "is not"
else:
     print("Please add Full-Time status to information.")
     
     
print("Sandy currently", ftEmp, " employed by the Department of Homeland Security as a", sandysJob)

print("\n\n\n")
print("Removing Keys from Dictionaries -------------------------")
print("Using the pop() method")

print(info.pop("job", None)) # check for job, else it prints "None"
print(info)

print(info.pop("occupation")) # Removes the key "occupation" from info
print(info)

#print(info.pop())
print(info)

print("\n\n\n")
print("Traversing Dictionaries---------------------")
"""
Format:
for key in dict:
    print(key, info[key])
"""

grades = {90 : 'A', 80 : 'B', 70 : 'C'}
print(list(grades.items()))

theKeys = list(grades.keys())
theKeys.sort()

for key in theKeys:
     print(key, grades[key])
     
def init_dict_1(n):
    ''' Initialize a dictionary with n key-value pairs. '''
    d = {}
    for i in range(n):
        x = i * 2
        d[i] = x
    return d

x = init_dict_1(100)

for items in x:
     print("Item", items, ":", x[items])
