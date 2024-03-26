import numpy as np

longString = "But consider your daughters. Only think what an establishment it would be for one of them."

print( len(longString))

# compute the number of characters in longString

count0 = 0
for string in longString:
    count0 += 1
print("Length:", count0)

count = 0
for string in longString:
    if string == " ":
        pass
    else:
        count += 1
print("Characters only:",count)

count1 = 0
for string in longString:
    if string != " ":
        count1 += 1
# print("Characters only:", count1)

uniqueLetters = []
for string in longString:
    if string not in uniqueLetters:
        uniqueLetters.append(string)
print("unique letters =", len(uniqueLetters), uniqueLetters)

letterList = []
for elem in uniqueLetters:
    letterList.append(elem)

letterList2 = list( uniqueLetters )

print(letterList)
print(letterList2)