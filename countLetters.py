filename = "pride2.txt"

with open(filename, "r", encoding='utf-8') as filehandler:
    n = 0
    uniqueLetters = set()
    while True:
        line = filehandler.readline()
        if not line:
            break
        n += 1
        for letter in line:
            uniqueLetters.add(letter)
        #print(n, line)
        #if n > 3:
        #    break
# print(f"Total {n} lines from {filename}: {len(uniqueLetters)} letters in the set {uniqueLetters}")

# 2. Count each letter, going through the txt file from the beginning.
# 2.1. Initialize the dictionary
counts = {}
for letter in uniqueLetters:
    counts[letter] = 0
# print(counts)

with open(filename, "r", encoding='utf-8') as file:
    n = 0
    while True:
        line = file.read()
        if not line:
            break
        n += 1

        for letter in line:
            counts[letter] += 1

        if n == 1:
            break

for key, value in counts.items():
    if value > 0:
        print(key, ":", value)