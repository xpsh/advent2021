
with open("input.txt","r") as f:
    grid = [[int(x) for x in line] for line in f.read().strip().split("\n")]

steps = 100
flashes = 0

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
            
height = len(grid)
width = len(grid[0])

#part 1
for s in range(steps):
    to_flash = []
    flashed = []
    for j in range(height):
        for i in range(width):
            grid[j][i] += 1
            if grid[j][i] > 9 and (i,j) not in flashed and (i,j) not in to_flash:
                to_flash.append((i,j))
                
    while to_flash:
        x,y = to_flash.pop(0)
        flashed.append((x,y))
        flashes += 1
        
        for r in range(8):
            nx = x + dx[r]
            ny = y + dy[r]
            if nx not in range(width) or ny not in range(height):
                continue
            
            grid[ny][nx] += 1
            
            if grid[ny][nx] > 9 and (nx,ny) not in flashed and (nx,ny) not in to_flash:
                to_flash.append((nx,ny))

    for x,y in flashed:
        grid[y][x] = 0

print(flashes)

#part 2
target = height * width
step = 100 # Assuming 100 steps is not enough to sync... otherwise comment out part 1 and set to 0
to_flash = []
flashed = []

while len(flashed) < target:
    step += 1
    to_flash = []
    flashed = []
    for j in range(height):
        for i in range(width):
            grid[j][i] += 1
            if grid[j][i] > 9 and (i,j) not in flashed and (i,j) not in to_flash:
                to_flash.append((i,j))
                
    while to_flash:
        x,y = to_flash.pop(0)
        flashed.append((x,y))
        
        for r in range(8):
            nx = x + dx[r]
            ny = y + dy[r]
            if nx not in range(width) or ny not in range(height):
                continue
            
            grid[ny][nx] += 1
            
            if grid[ny][nx] > 9 and (nx,ny) not in flashed and (nx,ny) not in to_flash:
                to_flash.append((nx,ny))

    for x,y in flashed:
        grid[y][x] = 0

print(step)
