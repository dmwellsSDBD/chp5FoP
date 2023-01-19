print("Dictionary to List Usint list() Funciton")
scoresDict = {'hw1' : 20, 'hw2' : 17, 'hw3' : 18, 'hw4' : 15}
scoresList = list(scoresDict)
print(scoresList)

print("List to Dictionary using the dict() Function")
listOData = [('quiz1', 3), ['quiz2', 12], ['quiz3', 34]]
dictOData = dict(listOData)
print(dictOData)

#alphaBad = dict(['a', 'b', 'c']) # try this to see the error
#print(alphaBad)
alphabet = dict([['a', 'apple'], ['b', 'banana'], ['c', 'cantaloupe']])
#alphabet = dict([['a', 'apple', 'apricot'], ['b', 'banana', 'blueberry'], ['c', 'cantaloupe', 'coconut']])
print(alphabet)

quizKeys = list(dictOData.keys())
for score in scoresDict.values():
    print(score /20.0)

listForm = list(alphabet.items())
print(listForm)