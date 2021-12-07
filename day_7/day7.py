
with open("input.txt","r") as f:
    data = [int(x) for x in f.read().split(",")]

min_x = 0
min_val = -1

left = min(data)
right = max(data)

#part 2 (modified from part 1)
for i in range(left,right + 1):
    total = 0
    for n in data:
        # original solution - takes a minute
        #total += sum(range(abs(n-i)+1))

        # new solution - got the formula from a reddit answer... was looking for something like this but didn't know off the top of my head
        na = abs(n-i)
        total += na*(na+1)//2
    if min_val < 0:
        min_val = total
    if total < min_val:
        min_val = total
        min_x = i # turns out this isn't even actually necessary...

print(min_val)
