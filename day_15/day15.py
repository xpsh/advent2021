
with open("input.txt","r") as f:
    data = f.read().strip()

gl = [[int(x) for x in line] for line in data.split("\n")]

w = len(gl[0])
h = len(gl)
#p1
g = {}
for j in range(h):
    for i in range(w):
        g[(i,j)] = gl[j][i]

#p2
g = {}
for l in range(5):
    for k in range(5):
        for j in range(h):
            for i in range(w):
                v = gl[j][i] + l + k
                while v > 9:
                    v -= 9
                g[(i+w*k,j+h*l)] = v

for i in range(5*h):
    print("".join([str(g[(i,j)]) for j in range(5*w)]))
        

rd = {(0,0):0}
to_visit = [(0,0)]

while to_visit:
    x,y = to_visit.pop(0)
    #print(x,y)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx not in range(5*w) or yy not in range(5*h):
            continue
        else:
            rr = rd[(x,y)] + g[(xx,yy)]
            if (xx,yy) in rd:
                if rd[(xx,yy)] > rr:
                    rd[(xx,yy)] = rr
                    to_visit.append((xx,yy))
            else:
                rd[(xx,yy)] = rr
                to_visit.append((xx,yy))
print(rd[(5*w-1,5*h-1)])
