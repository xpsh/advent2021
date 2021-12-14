import json

with open("input.txt","r") as f:
    rpolymer,r_rules = f.read().split("\n\n")

rules = {}
for r_rule in r_rules.strip().split("\n"):
    seq, ins = r_rule.split(" -> ")
    rules[seq]= ins

chars = []
for c in r_rules.strip().replace("\n","").replace(" -> ",""):
    if c not in chars:
        chars.append(c)
    

steps = 20
#f = rpolymer[-1]
#pd = {i:rpolymer[i] for i in range(len(rpolymer))}
n = 1

try:
    with open("twenties.json", "r") as f:
        twenties = json.load(f)
except:
    twenties = {}

if not twenties:
    for rule in rules:
        print(f"Rule {n} of {len(rules)}")
        n+=1
        f = rule[1]
        pd = {0:rule[0],1:rule[1]}
        for s in range(steps):
            np = {}
            ni = 0

            cd = {c:0 for c in chars}

            for i in range(len(pd)-1):
                np[ni] = pd[i]
                cd[np[ni]] += 1
                np[ni+1] = rules[pd[i] + pd[i+1]]
                cd[np[ni+1]] += 1
                ni += 2
            np[ni] = f
            cd[f] += 1
            pd = np
        
        for x in rule:
            cd[x] -= 1
        twenties[rule] = (cd,"".join(pd.values()))

    with open("twenties.json","w") as f:
        json.dump(twenties,f,indent=4)

f_l = len(rpolymer)
for i in range(40):
    if i == 20:
        f_l2 = f_l
    f_l = f_l*2-1

p = {i:rpolymer[i] for i in range(len(rpolymer))}
f = rpolymer[-1]
print("Finding 20th polymer")
ccounts = {x:rpolymer.count(x) for x in chars}
twenty_poly = ""
for i in range(len(p)-1):
    cd,ppoly = twenties[p[i]+p[i+1]]
    twenty_poly += ppoly[:-1]
    for x in ccounts:
        ccounts[x] += cd[x]
twenty_poly += f

print(f"Length of 20th polymer = {len(twenty_poly)} (expected {f_l2})")
p = {i:twenty_poly[i] for i in range(len(twenty_poly))}
print(len(p))
for i in range(len(p)-1):
    if i % 1000000 == 0:
        print(f"{i}/{len(p)}")
    cd,ppoly = twenties[p[i]+p[i+1]]
    for x in ccounts:
        ccounts[x] += cd[x]

counts = sorted(ccounts.values())
print(f"Final diff: {counts[-1]-counts[0]}")
