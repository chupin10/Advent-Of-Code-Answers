import sys
from typing import List, Tuple

import numpy as np


TESTS_P1 = (
    ('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83', 159),
    ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 135)
)

TESTS_P2 = (
    ('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83', 610),
    ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 410)
)


SIZE = 30000
STARTPOINT = np.array([15000, 15000])


def open_input() -> Tuple[List[int]]:
    with open('../inputs/day3.txt', 'r') as f:
        _wire1 = [Move(m) for m in f.readline().split(',')]
        _wire2 = [Move(m) for m in f.readline().split(',')]
    return _wire1, _wire2


class Move:
    def __init__(self, desc: str):
        self.dir = desc[0]
        self.mag = int(desc[1:])

    def apply_move(self, p0: np.ndarray) -> np.ndarray:
        if self.dir == 'R':
            return p0 + np.array([0, self.mag])
        if self.dir == 'L':
            return p0 + np.array([0, -self.mag])
        if self.dir == 'U':
            return p0 + np.array([self.mag, 0])
        if self.dir == 'D':
            return p0 + np.array([-self.mag, 0])


def manhattan_distance(p0: np.ndarray, p1: np.ndarray) -> float:
    return np.sum(np.abs(p1 - p0))


def apply_wire_routes(wire: List[Move]) -> np.ndarray:
    loc = np.full((SIZE, SIZE), 0, dtype=np.int32)
    pos0 = STARTPOINT.copy()
    steps = 0
    for m in wire:
        pos1 = m.apply_move(pos0)
        dp = pos1 - pos0
        # tuples to use for slicing the full location array
        ridxs = (np.min((pos0[0], pos1[0])), np.max((pos0[0], pos1[0]))) if dp[0] != 0 else (pos1[0],)
        cidxs = (np.min((pos0[1], pos1[1])), np.max((pos0[1], pos1[1]))) if dp[1] != 0 else (pos1[1],)
        if np.max((*ridxs, *cidxs)) > SIZE or np.min((*ridxs, *cidxs)) < 0:
            print(f'Array wrapped. Make it bigger\nridxs={ridxs} | cidxs={cidxs}')
            sys.exit()

        if m.dir in ['D', 'L']:
            newsteps = np.linspace(steps + m.mag, steps, m.mag + 1)
        else:
            newsteps = np.linspace(steps, steps + m.mag, m.mag + 1)

        if len(ridxs) > 1:
            # we started on step n, so replace these array values with incremental values
            loc[ridxs[0]:ridxs[1]+1, cidxs[0]] = np.min((loc[ridxs[0]:ridxs[1]+1, cidxs[0]], newsteps), axis=0)
            mask = loc[ridxs[0]:ridxs[1]+1, cidxs[0]] == 0  # nothing should be left at 0 though
            loc[ridxs[0]:ridxs[1]+1, cidxs[0]][mask] = newsteps[mask]
        else:
            loc[ridxs[0], cidxs[0]:cidxs[1]+1] = np.min((loc[ridxs[0], cidxs[0]:cidxs[1]+1], newsteps), axis=0)
            mask = loc[ridxs[0], cidxs[0]:cidxs[1]+1] == 0
            loc[ridxs[0], cidxs[0]:cidxs[1]+1][mask] = newsteps[mask]
        pos0 = pos1.copy()
        steps += m.mag
    return loc


if __name__ == '__main__':
    # examples
    for (t, p1_correct), (_, p2_correct) in zip(TESTS_P1, TESTS_P2):
        wire1 = [Move(m) for m in t.split('\n')[0].split(',')]
        wire2 = [Move(m) for m in t.split('\n')[1].split(',')]
        path1 = apply_wire_routes(wire1)
        path2 = apply_wire_routes(wire2)
        intersections = path1.astype(bool) & path2.astype(bool)
        xidxs, yidxs = np.where(intersections == True)
        dists = np.array([manhattan_distance(STARTPOINT, np.array([x, y])) for x, y in zip(xidxs, yidxs)])
        dists = dists[dists != 0]  # assume we don't allow the start point as an intersection
        print(f'Part 1 example result: {np.min(dists) == p1_correct}')  # check part 1
        # part 2
        minsteps = min(path1[intersections] + path2[intersections])
        print(f'Part 2 example result: {minsteps == p2_correct}')
        if not minsteps == p2_correct:
            print(minsteps, p2_correct)

    # part 1
    wire1, wire2 = open_input()
    path1 = apply_wire_routes(wire1)
    path2 = apply_wire_routes(wire2)
    intersections = path1.astype(bool) & path2.astype(bool)
    xidxs, yidxs = np.where(intersections == True)
    dists = np.array([manhattan_distance(STARTPOINT, np.array([x, y])) for x, y in zip(xidxs, yidxs)])
    dists = dists[dists != 0]  # assume we don't allow the start point as an intersection
    print(f'Part 1 answer: {np.min(dists)}')
    print(f'Part 2 answer: {min(path1[intersections] + path2[intersections])}')
