
with open("input.txt","r") as f:
    raw_called, raw_cards = f.read().split("\n\n",1)

called = [int(x) for x in raw_called.split(",")]

cards = [[int(num.strip()) for num in card.replace("\n"," ").split(" ") if num] for card in raw_cards.split("\n\n")]

hit_cards = [set() for x in cards]

def check_bingo(hits):
    wins = [{0,6,12,18,24},{4,8,12,16,20},{0,1,2,3,4},{5,6,7,8,9},{10,11,12,13,14},{15,16,17,18,19},{20,21,22,23,24},{0,5,10,15,20},{1,6,11,16,21},{2,7,12,17,22},{3,8,13,18,23},{4,9,14,19,24}]
    for win in wins:
        if hits & win == win:
            return True

# part 1
"""
bingo = False
for call in called:
    for i in range(len(cards)):
        if call not in cards[i]:
            continue
        index = cards[i].index(call)
        if index >= 0:
            hit_cards[i].add(index)

    for i in range(len(cards)):
        if check_bingo(hit_cards[i]):
            sum = 0
            for j in range(len(cards[i])):
                if j in hit_cards[i]:
                    continue
                else:
                    sum += cards[i][j]
            print(sum*call)
            bingo = True
            break
    if bingo:
        break
"""

# part 2

bingo_cards = []
done = False
for call in called:
    for i in range(len(cards)):
        if i in bingo_cards or call not in cards[i]:
            continue
        index = cards[i].index(call)
        hit_cards[i].add(index)

        if check_bingo(hit_cards[i]):
            bingo_cards.append(i)

        if len(bingo_cards) == len(cards):
            sum = 0
            for j in range(len(cards[i])):
                if j in hit_cards[i]:
                    continue
                else:
                    sum += cards[i][j]
            print(sum*call)
            done = True
            break
    if done:
        break
