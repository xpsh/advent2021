hex = open("input.txt").read().strip()

hs = "0123456789ABCDEF"
hd = {x:"0"*(4-len(bin(hs.index(x))[2:]))+bin(hs.index(x))[2:] for x in hs}

bn = ""
for h in hex:
    bn+=hd[h]

print(hex)
print(bn)
vs = [] # pt 1
code = bn
def parse_packet():
    global vs,code
    vb = code[:3]
    tb = code[3:6]
    v = int(vb,2)
    vs.append(v)
    t = int(tb,2)
        
    if t == 4:
        done = False
        i = 0
        n = ""
        while not done:
            chunk = code[5*i+6:5*(i+1)+6]
            if chunk[0] == '1':
                n += chunk[1:]
                i += 1
            else:
                n += chunk[1:]
                done = True
        val = int(n,2)
        code = code[5*(i+1)+6:]
        return val
    else:
        m = code[6]
        subs = []
        code = code[7:]
        if m == '0':
            l = int(code[:15],2)
            code = code[15:]
            sl = len(code)
            
            while sl - len(code) != l:
                subs.append(parse_packet())
        else:
            np = int(code[:11],2)
            code = code[11:]
            while len(subs) < np:
                subs.append(parse_packet())
        if t == 0:
            return sum(subs)
        elif t == 1:
            ans = 1
            for x in subs:
                ans *= x
            return ans
        elif t == 2:
            return min(subs)
        elif t == 3:
            return max(subs)
        elif t == 5:
            if subs[0] > subs[1]:
                return 1
            else:
                return 0
        elif t == 6:
            if subs[0] < subs[1]:
                return 1
            else:
                return 0
        elif t == 7:
            if subs[0] == subs[1]:
                return 1
            else:
                return 0

print(parse_packet())
