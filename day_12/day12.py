with open("input.txt","r") as f:
    data = f.read().strip().split("\n")

sc = set()
dests = {'start':[]}
for line in data:
    a,b = line.split("-")
    for x in [a,b]:
        if x.lower() == x and x not in ['start','end']:
            sc.add(x)

    if a == 'start':
        dests[a].append(b)
        continue
    if b == 'start':
        dests[b].append(a)
        continue
    
    if a in dests:
        dests[a].append(b)
    else:
        dests[a] = [b]

    if b == "end":
        continue
    
    if b in dests:
        dests[b].append(a)
    else:
        dests[b] = [a]
    
"""
#part 1
paths = set()
def find_path(c_path,node):
    global dests, sc, paths
    if node == 'end':
        paths.add(",".join(c_path + ['end']))
    elif node in sc and node in c_path:
        return
    elif node not in dests:
        return
    else:
        for dest in dests[node]:
            find_path(c_path + [node],dest)
  

find_path([],'start')
print(f"Part 1 Final count: {len(paths)}")
"""

#part 2
paths = set()
def get_all_paths(c_path,node):
    global dests,sc,paths

    if node == 'end':
        paths.add(",".join(c_path + ['end']))
        print(",".join(c_path+['end']))
        return
    exc = ['start']
    for x in sc:
        if (c_path+[node]).count(x) == 2:
            exc += [y for y in sc if y in (c_path+[node])]
    for dest in dests[node]:
        if dest not in exc:
            get_all_paths(c_path + [node],dest)
            
get_all_paths([],'start')


print("test ans",len(paths))
