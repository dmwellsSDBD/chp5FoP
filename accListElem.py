wordList = ['child', 'ball', 'hits', 'buys']
print(wordList[0], wordList[2], wordList[1])
print()
wordList[0] = 'wombat'
print(wordList[0], wordList[2], wordList[1])
print()
print("insert Example")

example = [1, 2]
example.insert(1, 10)
print(example)

print()
example.insert(3, 25)
print(example)

print()
print("append Example:")

example = [1, 2]
example.append(3)
print(example)

print()

print("extend Example")
example.extend([11, 12, 13])
print(example)

example = example + [14, 15]
print(example)

print()
print("pop example:")

print(example.pop())
print(example.pop(3))