
with open("input.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

opens = ["(", "[", "{", "<"]
closes = [")","]","}",">"]

score = {")":3,"]":57,"}":1197,">":25137}

error_score = 0
for line in data:
    t_opens = []
    for c in line:
        if c in opens:
            t_opens.append(c)
        elif c in closes:
            if not t_opens:
                error_score += score[c]
                break
            elif opens.index(t_opens[-1]) == closes.index(c):
                t_opens.pop(-1)
            else:
                error_score += score[c]
                break
            
print(error_score)

#part 2

corrections = {")":1,"]":2,"}":3,">":4}
correct_scores = []
for line in data:
    t_opens = []
    fail = False
    for c in line:
        if c in opens:
            t_opens.append(c)
        elif c in closes:
            if not t_opens:
                fail = True
                break
            elif opens.index(t_opens[-1]) == closes.index(c):
                t_opens.pop(-1)
            else:
                fail = True
                break
    c_score = 0
    while not fail and t_opens:
        c_score = c_score *5 + corrections[closes[opens.index(t_opens[-1])]]
        t_opens.pop(-1)
    if c_score > 0:
        correct_scores.append(c_score)

correct_scores.sort()
print(correct_scores[len(correct_scores)//2])
