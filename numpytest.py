import numpy as np

print("my numpy version: ", np.__version__)


randomList = []
for i in range(100_000):
    n = np.random.randint(1,20)
    randomList.append(n)
# print("randomList: ", randomList)

randomArray = np.random.randint(1, 20, size=10_000_000)
print("randomArray: ", randomArray.shape, randomArray.size)


# let's find out if there is 19 in the list.
count = 0
for number in randomArray:
    if number == 19:
        count += 1
        # print("co 19 nha thay")
# print("the list contains", count, "19s.")
# print(f"the list contains {count} 19s.")

for n in range(1,20):
    countAll = 0
    for number in randomArray:
        if number == n:
            countAll += 1
    print(n, ":", f"{countAll}")

print("Finished.")