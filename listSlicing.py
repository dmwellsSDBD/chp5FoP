lstA = ['ab', 'fr', 'ty', 'or', 'le', 'bo']

sub1 = lstA[2:5]
sub2 = lstA[0:2]
sub3 = lstA[:2]
sub4 = lstA[4:]

print(sub1)
print(sub2)
print(sub3)
print(sub4)

copyLstA = lstA[:]
print(copyLstA)

altA = copyLstA[0:6:2]
print(altA)