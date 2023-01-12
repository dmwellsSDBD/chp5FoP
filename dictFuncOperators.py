letterFreq = {'a' : 195, 'r' : 22, 'e': 256, 't' : 166, 'l' : 103, 'x' : 2}

print("Length: ", len(letterFreq))

print("Delete one of our pairs:")
del letterFreq['l']

print("Length: ", len(letterFreq))

if 't' in letterFreq:
    letterFreq['t'] = letterFreq['t'] +1
if 'z' not in letterFreq:
    letterFreq['z'] = 1
    
    
print(len(letterFreq))