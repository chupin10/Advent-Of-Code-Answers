with open("/Users/christopherauld/Desktop/AOC2018/data/day2/input.txt", "r") as file:
    s = [line.strip("\n") for line in file]

# Part 1
out = {}

for group in s:
    for char in group:
        if group.count(char) > 1:
            out[group] = [0, 0]
        if group.count(char) == 2:
            out[group][0] = 1
        if group.count(char) == 3:
            out[group][1] = 1

twos = 0
threes = 0
for key, val in out.items():
    twos += val[0]
    threes += val[1]
print(twos * threes)

# Part 2
o = {}
for i, group in enumerate(s):
    o[i] = group

def is_off_by_one(a, b):
    num_wrong = 0
    for i, char in enumerate(a):
        if char != b[i]:
            num_wrong += 1
        if num_wrong > 1:
            return False
    if num_wrong == 1:
        return True
    if num_wrong != 1:
        return False

for key, val in o.items():
    for k, v in o.items():
        found = is_off_by_one(val, v)
        if found:
            print(k, v, key, val)