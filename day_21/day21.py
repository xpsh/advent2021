if __name__ == '__main__':
    with open('input.txt','r') as f:
        r_data = f.read()

    pos = {}
    for line in r_data.strip().split('\n'):
        pos[line.split()[1]] = int(line.split()[-1])

    max_score = 0
    scores = {}
    for player in pos:
        scores[player] = 0

    die = 0
    rolls = 0
    won = False
    while not won:
        for player in pos:
            move = 0
            for i in range(3): 
                die+=1
                if die == 101:
                    die = 1
                move += die
                rolls += 1
            pos[player] = (pos[player]+move-1)%10 + 1
            scores[player] += pos[player]
            if scores[player] >= 1000:
                won = True
                break

    losing_score = 1000
    for player in scores:
        if scores[player] < losing_score:
            losing_score = scores[player]
    print(losing_score*rolls)

    # Part 2
    for line in r_data.strip().split('\n'):
        pos[line.split()[1]] = int(line.split()[-1])

    states = {(pos['1'],pos['2'],0,0):1}
    wins = {'1':0, '2':0}
    while states:
        new_states = {}
        for state in states:
            p1,p2,s1,s2 = state
            count = states[state]
            for i in range(1,4):
                for j in range(1,4):
                    for k in range(1,4):
                        pp1 = (p1+i+j+k-1)%10+1
                        ss1 = s1 + pp1
                        if ss1 >= 21:
                            wins['1'] += count
                        else:
                            for l in range(1,4):
                                for m in range(1,4):
                                    for n in range(1,4):
                                        pp2 = (p2+l+m+n-1)%10+1
                                        ss2 = s2 + pp2
                                        if ss2 >= 21:
                                            wins['2'] += count
                                        else:
                                            new_state = (pp1,pp2,ss1,ss2)
                                            if new_state in new_states:
                                                new_states[new_state] += count
                                            else:
                                                new_states[new_state] = count
        states = new_states
    
    print(max(wins.values()))

                    
