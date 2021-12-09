
with open("input.txt","r") as f:
    heatmap = [[int(y) for y in x.strip()] for x in f.readlines()]

height = len(heatmap)
width = len(heatmap[0])

low_sum = 0

for i in range(height):
    for j in range(width):
        val = heatmap[i][j]
        if i+1 in range(height):
            if heatmap[i+1][j] <= val:
                continue
        if i-1 in range(height):
            if heatmap[i-1][j] <= val:
                continue
        if j+1 in range(width):
            if heatmap[i][j+1] <= val:
                continue
        if j-1 in range(width):
            if heatmap[i][j-1] <= val:
                continue
        low_sum += val+1
print(low_sum)

#part 2   
basins = []
for i in range(height):
    for j in range(width):
        val = heatmap[i][j]
        if i+1 in range(height):
            if heatmap[i+1][j] <= val:
                continue
        if i-1 in range(height):
            if heatmap[i-1][j] <= val:
                continue
        if j+1 in range(width):
            if heatmap[i][j+1] <= val:
                continue
        if j-1 in range(width):
            if heatmap[i][j-1] <= val:
                continue

        basin = {(j,i)}
        unchecked = [(j,i)]
        while unchecked:
            x,y = unchecked[0]

            if (x+1,y) not in basin and x+1 in range(width) and heatmap[y][x+1] != 9:
                basin.add((x+1,y))
                unchecked.append((x+1,y))
            if (x-1,y) not in basin and x-1 in range(width) and heatmap[y][x-1] != 9:
                basin.add((x-1,y))
                unchecked.append((x-1,y))
            if (x,y+1) not in basin and y+1 in range(height) and heatmap[y+1][x] != 9:
                basin.add((x,y+1))
                unchecked.append((x,y+1))
            if (x,y-1) not in basin and y-1 in range(height) and heatmap[y-1][x] != 9:
                basin.add((x,y-1))
                unchecked.append((x,y-1))

            unchecked.pop(0)
        basins.append(len(basin))

basins.sort()

print(basins[-1]*basins[-2]*basins[-3])
        
                    
            
