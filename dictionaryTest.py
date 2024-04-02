import numpy as np

d = {"a": 0, "b": 1, "c": 2}

keyvalue = dict()

print(d)

for key, value in d.items(): # a = key, 0 = value
    # print(key, value)
    print(f"{key} : {value}")

print(d['a'], d['c'])

d['a'] += 10
d['c'] += 20
print(d['a'], d['c'])

kv = {10: 0, 20: 1, 30: "hello"}
print("keys: ", kv.keys())
print("value: ", kv.values())

kv['x'] = 0
print(kv)