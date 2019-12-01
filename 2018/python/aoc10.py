import matplotlib.pyplot as plt
import numpy as np  

with open("/Users/christopherauld/Desktop/AOC2018/data/day10/input.txt", "r") as file:
    s = [line.strip("\n").replace("position=<", " ").replace("velocity=<", " ").replace(">", " ").replace(",", " ") for line in file]

points = []
for line in s:
    l = [t for t in line.split(" ") if t is not ""]
    pos = np.array([int(l[0]), int(l[1])])
    vel = np.array([int(l[2]), int(l[3])])
    points.append([pos, vel])

def update_pos(points):
    for p in points:
        p[0] += p[1]

def get_bbox_size(points):
    minx = min([p[0][0] for p in points])
    miny = min([p[0][1] for p in points])
    maxx = max([p[0][0] for p in points])
    maxy = max([p[0][1] for p in points])
    return maxx - minx, maxy - miny


# check to see how the bounding box is changing, look for minumum and then use that below as starting point
bbs = []
for p in points:
    p[0] += p[1] * 10000
for i in range(10000, 11000):
    bbs.append(get_bbox_size(points))
    update_pos(points)
    print(i)
        
plt.figure()
plt.plot(bbs)
plt.show()


# update positions
for p in points:
    p[0] += p[1] * 10639

fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.scatter([p[0][0] for p in points], [p[0][1] for p in points])
plt.show()