import heapq

with open("input.txt","r") as f:
    data = f.read().strip()

gl = [[int(x) for x in line] for line in data.split("\n")]

w = len(gl[0])
h = len(gl)
n = 5# p2
#n = 1 # p1
g = {}
for l in range(n):
    for k in range(n):
        for j in range(h):
            for i in range(w):
                v = gl[j][i] + l + k
                while v > 9:
                    v -= 9
                g[(i+w*k,j+h*l)] = v        

to_visit = [(0,0,0)]
visited = {}
while to_visit:
    v,x,y = heapq.heappop(to_visit)

    if (x,y) in visited:
        continue
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx not in range(n*w) or yy not in range(n*h):
            continue
        rr = v + g[(xx,yy)]
        heapq.heappush(to_visit,(rr,xx,yy))
        
    visited[(x,y)] = v
    if (x,y) == (n*w-1,n*h-1):
        print(visited[(x,y)])
        break
