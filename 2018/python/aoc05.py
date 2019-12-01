import collections


with open("/Users/christopherauld/Desktop/AOC2018/data/day05/input.txt", "r") as file:
    s = file.read()


def look_for_reaction(s):
    for i in range(len(s)):
        char = s[i]
        if i < len(s) - 1 and char.lower() == s[i + 1].lower():
            char2 = s[i + 1]
            if (char.isupper() and char2.islower()) or (char.islower() and char2.isupper()):
                s = s[: i] + s[i+2 :]
                return True, s
    return False, s


repeat_found = False # set to true to solve part 1
while repeat_found:
    repeat_found, s = look_for_reaction(s)

print(len(s)) # answer to part 1

s_low = s.lower()
results = collections.Counter(s_low)

s_full = s
for letter in results.keys():
    repeat_found = True
    s = s_full.replace(letter, "").replace(letter.upper(), "")
    while repeat_found:
        repeat_found, s = look_for_reaction(s)
    print(letter, len(s))