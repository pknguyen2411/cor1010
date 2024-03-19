# random numbers!
import random
import numpy as np

# print a list of random numbers:
listOfRandomNumbers = []
for i in range(1,100):
    x = random.randint(1,100)
    listOfRandomNumbers.append(x)
print(listOfRandomNumbers)

# compute the sum of the list
# solution 1:
total = 0
for number in listOfRandomNumbers:
    total = total + number
print("total: ", total)
# solution 2:
totalsum = sum(listOfRandomNumbers)
print("total: ", totalsum)

# length of list
list2 = [random.randint(1,20) for i in range(100)]
print(list2)
print("length of list2 is ", len(list2))

# npnumber = np.random.