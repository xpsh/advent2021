

with open("input.txt","r") as f:
    rdots,rfolds = f.read().strip().split("\n\n")

dots = rdots.split("\n")
dots = {(int(line.split(",")[0]),int(line.split(",")[1])) for line in dots}

rfolds = rfolds.split("\n")
folds = []
for line in rfolds:
    rd = line.split(" ")[2]
    folds.append((rd.split("=")[0],int(rd.split("=")[1])))

#p1
def fold(axis,num,card):
    newcard = set()
    if axis == "x":
        for x,y in list(card):
            if x > num:
                newcard.add((num-(x-num),y))
            else:
                newcard.add((x,y))
    else:
        for x,y in card:
            if y > num:
                newcard.add((x,num-(y-num)))
            else:
                newcard.add((x,y))
    return newcard

axis,num = folds[0]
print(len(fold(axis,num,dots)))

#p2
for f in folds:
    axis,num = f
    dots = fold(axis,num,dots)

width = 0
height = 0
for x,y in dots:
    if x > width:
        width = x
    if y > height:
        height = y

grid = [[" " for x in range(width+1)] for y in range(height+1)]
for x,y in dots:
    grid[y][x] = "#"

for line in grid:
    print("".join(line))
