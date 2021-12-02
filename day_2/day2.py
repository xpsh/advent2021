# part 1
with open("input.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

directions = {'forward':[1,0],'up':[0,-1], 'down':[0,1]}

position = (0,0)
for line in data:
    dir,num = line.split()
    x,y = position
    dx,dy = [e*int(num) for e in directions[dir]]
    position = (x+dx,y+dy)

#print("Position: ", position)
#print(position[0]*position[1])


# part 2
position = (0,0,0) # third one is "aim"

for line in data:
    dir,num = line.split()
    x,y,a = position
    dx,da = [e*int(num) for e in directions[dir]]
    position = (x+dx, y+dx*a, a+da)

print(position[0]*position[1])
