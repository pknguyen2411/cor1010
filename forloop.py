

names = ["Tam", "Dau", "Tom", "Pk", "Hanh", "Hoa"]

print( names[0] )
print( names[1] )

names.append("Ngo")

print(names)

second_names = ["Xam"] + ["Tad"] + names
print(second_names)

print("-----")
for string in names:
    print("Anh yeu " + string)
    print(string[0] + "  la chu cai dau cua ten nguoi anh yeu")
    for c in string:
        print(c)
print("Finished.")

print("-----")
for k in [0, 1, 2, 3 ,4, 5, 6]:
    print(k, names[k])

print("-----")
for k in range(7):
    print(k, names[k])

hundnames = [ f"name_{i}" for i in range(100) ]
print(hundnames)
