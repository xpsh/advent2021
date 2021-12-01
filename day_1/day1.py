import re

with open("input1.txt","r") as f:
    data1 = [int(x.strip()) for x in f.readlines()]

increase = 0

for i in range(len(data1)):
    if i >= 1:
        if data1[i] > data1[i-1]:
            increase += 1

print(increase)

trincrease= 0
for i in range(len(data1)):
    if i >= 3:
        if data1[i] > data1[i-3]:
            trincrease += 1

print(trincrease)
