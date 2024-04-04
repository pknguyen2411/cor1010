# function
import numpy as np
import matplotlib.pyplot as plt

def add(a, b, c):
    "a, b, c are all numbers: int, float"
    result = a + b + c
    return result

i = 1
j = 2
k = 3

z = add(i, j, k)
print(i, j, k, "=", z)


def getuniqueLetters(string):
    " string: a str type input"
    listofuniqueLetters = []
    for ch in string:
        if ch not in listofuniqueLetters:
            listofuniqueLetters.append(ch)
    return listofuniqueLetters

myString = "I like 용덕"
myuniqueLetters = getuniqueLetters(myString)
print(myuniqueLetters)

myULsorted = sorted(myuniqueLetters)
print(myULsorted)

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.show()