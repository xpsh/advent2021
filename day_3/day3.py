import math

with open("input.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

bit_count = [0 for x in data[0]]

for line in data:
    for i in range(len(line)):
        bit_count[i] += int(line[i])

gam = ""
eps = ""
for cnt in bit_count:
    if cnt >= math.ceil(len(data)/2):
        gam += "1"
        eps += "0"
    else:
        gam += "0"
        eps += "1"

        
gam = int(gam,2)
eps = int(eps,2)

print(gam*eps)

# part 2
bit_count = len(data[0])

oxy_rem = [x for x in data]
carb_rem = [x for x in data]

ratings = [oxy_rem,carb_rem]
final_ratings = []
for j in range(len(ratings)):
    rating_data = ratings[j]
    for i in range(bit_count):
        key = int("0"*i + "1" + "0"*(bit_count-i-1),2)
        count = 0
        for line in rating_data:
            count += ((int(line,2) & key) >> (bit_count-i-1))

        new_rating_data = []
        for line in rating_data:
            if count >= math.ceil(len(rating_data)/2):
                if line[i] != str(j):
                    new_rating_data.append(line)
            elif line[i] == str(j):
                new_rating_data.append(line)
        rating_data = new_rating_data
        if len(rating_data) == 1:
            break
        
    final_ratings.append(rating_data[0])
    
print(final_ratings)
print(int(final_ratings[0],2) * int(final_ratings[1],2))
                        
        
