filename = "pride2.txt"

filehandler = open(filename, "r", encoding='utf-8') # w = write, r = read

n = 0
uniqueLetters = []
while True:
    line = filehandler.readline()
    if not line:
        break
    n += 1
    for letters in line:
        if letters not in uniqueLetters:
            uniqueLetters.append(letters)

filehandler.close()

print("unique letters =", len(uniqueLetters), uniqueLetters)
print(n)