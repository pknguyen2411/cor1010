import numpy as np

numberArray = np.random.randint(0, 10, size=20)
print(numberArray)

# to make a group of unique numbers

uniqueList = []
for number in numberArray:
    if number in uniqueList:
        pass
    else:
        uniqueList.append(number)
print("unique: ", uniqueList)

uniqueList2 = list() # == []
for number in numberArray:
    if number not in uniqueList2:
        uniqueList2.append(number)
print("unique: ", uniqueList2)

myList = []
myList2 = list()

# set, dict
uniqueSet = set()
for num in numberArray:
    uniqueSet.add(num)
print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=" ")
print()