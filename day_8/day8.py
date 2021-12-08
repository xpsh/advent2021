
with open("input.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

#part 1
count = 0
for d in data:
    digits,code = d.split("|")
    digits = [digit.strip() for digit in digits.strip().split(" ")]
    code = [num.strip() for num in code.strip().split(" ")]
    for num in code:
        if len(num) in [2,3,4,7]:
            count += 1

print(count)            

# part 2
patterns = {"abcefg":"0","cf":"1","acdeg":"2","acdfg":"3","bcdf":"4","abdfg":"5","abdefg":"6","acf":"7","abcdefg":"8","abcdfg":"9"}

letters = "abcdefg"

total = 0
for d in data:
    digits,code = d.split("|")
    digits = [digit.strip() for digit in digits.strip().split(" ")]
    code = [num.strip() for num in code.strip().split(" ")]

    for digit in digits:
        if len(digit) == 2:
            one = digit
        elif len(digit) == 3:
            seven = digit
        elif len(digit) == 4:
            four = digit

    # find out which letter corresponds to which
    decoded = {x:"" for x in letters}

    for x in seven:
        if x not in one:
            decoded[x] = "a"
    
    for letter in letters:
        count = "".join(digits).count(letter)
        if count == 6:
            decoded[letter] = "b"
        elif count == 4:
            decoded[letter] = "e"
        elif count == 9:
            decoded[letter] = "f"
        elif count == 8:
            if not decoded[letter]:
                decoded[letter] = "c"
        elif count == 7:
            if letter in four:
                decoded[letter] = "d"
            else:
                decoded[letter] = "g"

    output = ""
    for num in code:
        decoded_num = [decoded[x] for x in num]
        output += patterns["".join(sorted(decoded_num))]
    total += int(output)
    
print(total)
