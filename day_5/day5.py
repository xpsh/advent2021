import re

with open("input.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

counts = {}
for line in data:
    start, end = re.findall(r"\d+,\d+",line)
    startx, starty = [int(x) for x in start.split(",")]
    endx,endy = [int(x) for x in end.split(",")]
    
    #horizontal
    if startx == endx:
        if starty > endy:
            lowery = endy
            highery = starty
        else:
            lowery = starty
            highery = endy
        points = [(startx,y) for y in range(lowery,highery+1)]

    #vert
    elif starty == endy:
        if startx > endx:
            lowerx = endx
            higherx = startx
        else:
            lowerx = startx
            higherx = endx
        points = [(x,starty) for x in range(lowerx,higherx+1)]

    else:
        points = []
        number = abs(startx-endx) + 1
        if endx > startx:
            if endy > starty:
                dir = [1,1]
            else:
                dir = [1,-1]
        else:
            if endy > starty:
                dir = [-1,1]
            else:
                dir = [-1,-1]
        for i in range(number):
            points.append((startx+dir[0]*i,starty+dir[1]*i))
        
        
    for point in points:
        if point in counts:
            counts[point] += 1
        else:
            counts[point] = 1

num = 0
for count in counts:
    if counts[count] >= 2:
        num+=1

print(num)
