with open("/Users/christopherauld/Desktop/AOC2018/data/day1/aoc1.txt", "r") as file:
    freqs = [int(line.strip("\n")) for line in file]
# Part 1
print(sum(freqs))
# Part 2
pattern = set()
new_freq = None
last_freq = 0
i = 0
while not new_freq in pattern:
    pattern.add(last_freq)
    new_freq = int(freqs[i] + last_freq)
    i = i + 1 if i < len(freqs) - 1 else 0
    if new_freq in pattern:
        print(new_freq)
        pattern.add(new_freq)
    last_freq = new_freq