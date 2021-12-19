import math
import sys


class Pair:
    def __init__(self,parent=None):
        self.parent = parent
        self.left = None
        self.right = None
    
    def set_l(self,left):
        self.left = left
    def set_r(self,right):
        self.right = right

    def get_d(self):
        if self.parent:
            return self.parent.get_d()+1
        else:
            return 0
    def set_parent(self,parent):
        self.parent = parent

    def add_rightmost(self,v):
        if isinstance(self.right, Pair):
            return self.right.add_rightmost(v)
        else:
            self.right += v
    def add_leftmost(self,v):
        if isinstance(self.left, Pair):
            self.left.add_leftmost(v)
        else:
            self.left += v
    def print(self):
        s = "["
        if isinstance(self.left,int):
            s += str(self.left)
        else:
            s += self.left.print()
        s += ","
        if isinstance(self.right,int):
            s += str(self.right)
        else:
            s += self.right.print()
        s += "]"
        return s
        
def parse_pair(eq,parent=None):
    if eq.isnumeric():
        return int(eq)
    neq = eq[1:-1]
    d = 0
    np = Pair(parent)
    for i in range(len(neq)):
        if neq[i] == "[":
            d += 1
        elif neq[i] == "]":
            d -= 1            
        elif neq[i] == "," and d == 0:
            np.set_l(parse_pair(neq[:i],np))
            np.set_r(parse_pair(neq[i+1:],np))
            break
            
    return np

def explode(node):
    if isinstance(node.left,Pair):
        explode(node.left)
    elif isinstance(node.right,Pair):
        explode(node.right)
    elif node == node.parent.left:
        if isinstance(node.parent.right,Pair):
            node.parent.right.add_leftmost(node.right)
        else:
            node.parent.right += node.right
        cn = node.parent
        while True:
            if cn.parent == None:
                break
            elif cn == cn.parent.right:
                if isinstance(cn.parent.left,Pair):
                    cn.parent.left.add_rightmost(node.left)
                else:
                    cn.parent.left += node.left
                break
            else:
                cn = cn.parent
        node.parent.set_l(0)
            
    else:
        if isinstance(node.parent.left,Pair):
            node.parent.left.add_rightmost(node.left)
        else:
            node.parent.left += node.left
        cn = node.parent
        while True:
            if cn.parent == None:
                break
            elif cn == cn.parent.left:
                if isinstance(cn.parent.right,Pair):
                    cn.parent.right.add_leftmost(node.right)
                else:
                    cn.parent.right += node.right
                break
            else:
                cn = cn.parent
        node.parent.set_r(0)

def split(node):
    done = False
    if isinstance(node.left,int) and node.left > 9:
        nn = Pair(node)
        nn.set_l(math.floor(node.left/2))
        nn.set_r(math.ceil(node.left/2))
        node.set_l(nn)
        return True
        
    elif isinstance(node.left,Pair):
        done = split(node.left)

    if not done and isinstance(node.right,int) and node.right > 9:
        nn = Pair(node)
        nn.set_l(math.floor(node.right/2))
        nn.set_r(math.ceil(node.right/2))
        node.set_r(nn)
        return True
    
    elif not done and isinstance(node.right,Pair):
        done = split(node.right)

    return done
    
    

def find_nodes(start):
    nodes = [start]
    if isinstance(start.left,Pair):
        nodes += find_nodes(start.left)
    if isinstance(start.right,Pair):
        nodes += find_nodes(start.right)
    return nodes

def add_nodes(na,nb):
    np = Pair(None)
    na.set_parent(np)
    nb.set_parent(np)
    np.set_l(na)
    np.set_r(nb)
    return np

def reduce(node):
    changed = True
    while changed:
        changed = False
        all_n = find_nodes(node)
        for n in all_n:
            if n.get_d() == 4:
                changed = True
                explode(n)
        if changed:
            continue
        else:
            changed = split(node)

            
def magnitude(node):
    if isinstance(node,int):
        return node
    else:
        return 3*magnitude(node.left) + 2*magnitude(node.right)


data = []
for line in open("input.txt"):
    data.append(line.strip())
"""
# part 1
eq = None
for line in data:
    if not eq:
        eq = parse_pair(line)
    else:
        nn = parse_pair(line)
        eq = add_nodes(eq,nn)
        reduce(eq)
print(eq.print())
print(magnitude(eq))

"""
# part 2
mags = 0
for line in data:
    for nine in data:
        if line == nine:
            continue

        l = parse_pair(line)
        r = parse_pair(nine)
        print(f'checking {l.print()}')
        print(f'and {r.print()}')
        eq = add_nodes(l,r)
        reduce(eq)
        m = magnitude(eq)
        print(f'magnitude: {m}')
        if m > mags:
            mags = m

print(mags)

"""
# part 2
p = parse_pair(data[0])
for line in data[1:]:
    n = parse_pair(line)
    print(p.print())
    print(n.print())
    p = add_nodes(p,n)
    reduce(p)
    print(p.print())
    print()
    print()

na = parse_pair("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]")
nb = parse_pair("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]")

eq = add_nodes(na,nb)
reduce(eq)
print(eq.print())
eq = add_nodes(eq,parse_pair("[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]"))
reduce(eq)
print(eq.print())
"""
