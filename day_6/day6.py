
with open("input.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

fishes = [int(x) for x in data[0].split(',')]

#part 1
"""
days = 256
for day in range(days):
    new_fishes = []
    for fish in fishes:
        if fish >= 1:
            new_fishes.append(fish-1)
        elif fish == 0:
            new_fishes.append(6)
            new_fishes.append(8)
    fishes = new_fishes
"""

#part 2
days = 256

day_dict = {}
def make_fish(day_dict,start_day,days,num):
    day = start_day+9
    while day <= days:
        if day in day_dict:
            day_dict[day]+= num
        else:
            day_dict[day] = num
        day += 7
    
for fish in fishes:
    day = fish+1
    while day <= days:
        if day in day_dict:
            day_dict[day]+=1
        else:
            day_dict[day] = 1
        day += 7
    
num_fish = len(fishes)
for day in range(days):
    if day+1 in day_dict:
        num_fish += day_dict[day+1]
        make_fish(day_dict,day+1,days,day_dict[day+1])
print(num_fish)
