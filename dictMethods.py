letterFreq = {"a" : 195, "r" : 22, "e" : 256, "t" : 166, "l" : 103, "x" : 2}
print(letterFreq.get('r'), letterFreq['r'])
#print(letterFreq.get('q'), letterFreq['q'])
#print(letterFreq['q'])
lf = letterFreq.copy()
print("Original letterFreq:", letterFreq)
print("New Copy:", lf)

lf.update({'y':15, 'z':1})
lf.update([('a', 12), ('b', 232), ('c', 25)])
lf.update(m = 158, n = 89)
print("Updated copy: ", lf)

print("Updated letterFreq????", letterFreq)