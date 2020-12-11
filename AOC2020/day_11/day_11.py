import numpy as np

from AOC2020.helpers import GIT_DIR


FLOOR = 0
EMPTY = 1
OCCUPIED = 2


def parse_str(_s) -> np.ndarray:

    def str_to_int(_seat: str) -> int:
        if _seat == 'L':
            return EMPTY
        elif _seat == '#':
            return OCCUPIED
        else:
            return FLOOR

    data = [[str_to_int(seat) for seat in row] for row in _s.strip().split('\n')]
    return np.array(data, dtype=int)


def open_input() -> list[int]:
    with open(f'{GIT_DIR}/day_10/input.txt', 'r') as fh:
        inp = fh.read()
    inp = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    return parse_str(inp)


def neighbors_occupied(x: int, y: int, arr: np.ndarray) -> bool:
    for xd in (0, 1, -1):
        if x + xd < 0 or x + xd > arr.shape[0]:
            continue
        for yd in (0, 1, -1):
            if y + yd < 0 or y + yd > arr.shape[1]:
                continue
            try:
                if arr[x + xd, y + yd] == OCCUPIED:
                    return True
            except IndexError:
                continue
    return False


def adjacent_empty(x: int, y: int, arr: np.ndarray) -> bool:
    num_o = 0
    for xd in (0, 1, -1):
        if x + xd < 0 or x + xd > arr.shape[0]:
            continue
        for yd in (0, 1, -1):
            if y + yd < 0 or y + yd > arr.shape[1]:
                continue
            try:
                if arr[x + xd, y + yd] == OCCUPIED:
                    num_o += 1
            except IndexError:
                continue
    return num_o >= 4


def apply_rules(arr: np.ndarray) -> np.ndarray:
    _arr = arr.copy()
    empty_seats = np.where(arr == EMPTY)
    occupied_seats = np.where(arr == OCCUPIED)

    for x, y in zip(empty_seats[0], empty_seats[1]):
        if not neighbors_occupied(x, y, arr):
            _arr[x, y] = OCCUPIED

    for x, y in zip(occupied_seats[0], occupied_seats[1]):
        if adjacent_empty(x, y, arr):
            _arr[x, y] = EMPTY

    return _arr


if __name__ == '__main__':
    grid = open_input()
    print(grid)
    floormask = (grid != FLOOR).astype(int)
    print(floormask)
    oldgrid = grid.copy()
    grid = apply_rules(grid)
    count = 1
    while not np.array_equal(grid, oldgrid):
        oldgrid = grid.copy()
        grid = apply_rules(grid)
        count += 1
    print(count)
