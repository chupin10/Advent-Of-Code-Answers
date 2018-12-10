import numpy as np  

with open("/Users/christopherauld/Desktop/AOC2018/data/day3/input.txt", "r") as file:
    s = [line.strip("\n") for line in file]

s2 = [t.split(" ") for t in s]

claims = {}
for c in s2:
    claims[int(c[0].replace("#", ""))] = {
        "left": int(c[2].split(',')[0]),
        "top": int(c[2].split(',')[1].strip(":")),
        "width": int(c[3].split('x')[0]),
        "height": int(c[3].split('x')[1]),
        "has_overlap": False
    }

fabric = np.full((1000, 1000), 0, dtype = int)
fabric_claimer = np.full((1000, 1000), 0, dtype = int)

def fill_grid(c, name):
    #start = np.array([c["left"], c["top"]])
    #end = np.array([c["width"], c["height"]]) + start
    for i in range(c["width"]):
        for j in range(c["height"]):
            fabric[j + c["top"], i + c["left"]] += 1
            if fabric_claimer[j + c["top"], i + c["left"]] == 0:
                fabric_claimer[j + c["top"], i + c["left"]] = name
            elif fabric_claimer[j + c["top"], i + c["left"]] != -1:
                claims[fabric_claimer[j + c["top"], i + c["left"]]]["has_overlap"] = True
                fabric_claimer[j + c["top"], i + c["left"]] = -1 
                c["has_overlap"] = True
            else:
                c["has_overlap"] = True


for key, item in claims.items():
    fill_grid(item, key)

for key, item in claims.items():
    if not item["has_overlap"]:
        # Part 2 answer
        print(key)

import matplotlib.pyplot as plt 
fabric[fabric <= 1] = 0
fabric[fabric > 1] = 1
plt.imshow(fabric)

count = 0
for row in fabric:
    for col in row:
        if col == 1:
            count +=1
# Part 1 answer
print(count)

plt.show()