
data = open("input.txt").read().strip()

data = data.split(": ")[1]
rx = data.split(", ")[0].split("=")[1]
ry = data.split(", ")[1].split("=")[1]

xi,xf = [int(x) for x in rx.split("..")]
yi,yf = [int(x) for x in ry.split("..")]


def shoot(vx,vy):
    global xi,xf,yi,yf
    vx,vy = vx,vy
    x,y = 0,0
    maxy = 0
    while y >= yi and x <= xf:
        x += vx
        y += vy
        if y > maxy:
            maxy = y
        if x in range(xi,xf+1) and y in range(yi,yf+1):
            return maxy
        
        if vx > 0:
            vx -=1
        elif vx < 0:
            vx += 1
        vy -= 1
    return -1

max = 0
r = 200 # tried a few values
vels = []
for i in range(1,xf+1):
    for j in range(yi,r):
        mmy = shoot(i,j)
        if mmy >= 0:
            vels.append((i,j))
print(f"for {r}: {len(vels)}")
