import sys
from typing import List


def open_input() -> List[int]:
    with open('../inputs/day2.txt', 'r') as f:
        return [int(val) for val in f.read().split(',')]


def one(_curidx: int, vals: List[int]) -> None:
    idxin1 = vals[_curidx + 1]
    idxin2 = vals[_curidx + 2]
    idxout = vals[_curidx + 3]
    vals[idxout] = vals[idxin1] + vals[idxin2]


def two(_curidx: int, vals: List[int]) -> None:
    idxin1 = vals[_curidx + 1]
    idxin2 = vals[_curidx + 2]
    idxout = vals[_curidx + 3]
    vals[idxout] = vals[idxin1] * vals[idxin2]


def step(_curidx: int) -> int:
    return _curidx + 4


def init_alarm(vals: List[int]) -> None:
    vals[1] = 12
    vals[2] = 2


def finish(_curidx: int, vals: List[int]) -> None:
    print(f'Final index {_curidx}. Pos 0 val = {vals[0]}')


OPCODES = {
    1: one,
    2: two,
    99: finish
}

# input - output
EXAMPLES = [
    ([1,0,0,0,99], [2,0,0,0,99]),
    ([1,9,10,3,2,3,11,0,99,30,40,50], [3500,9,10,70,2,3,11,0,99,30,40,50]),
    ([2,3,0,3,99], [2,3,0,6,99]),
    ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
    ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])
]


def run_instructions(_data: List[int]) -> None:
    curidx = 0
    while True:
        if _data[curidx] not in [1, 2, 99]:
            print(f'Something has gone wrong, opcode = {_data[curidx]}')
            sys.exit()
        action = _data[curidx]
        OPCODES[action](curidx, _data)
        curidx = step(curidx)
        if curidx >= len(_data) or action == 99:
            break


if __name__ == '__main__':
    # examples
    print('EXAMPLES:')
    for (data, result) in EXAMPLES:
        run_instructions(data)
        print(data == result)
    # part 1
    data = open_input()
    init_alarm(data)
    print('\nPART 1:')
    run_instructions(data)
    # part 2
    def printless_finish(foo, bar):
        return
    OPCODES[99] = printless_finish  # remove brute force print outs
    print('\nPART 2:')
    for noun in range(100):
        for verb in range(100):
            data = open_input()
            data[1] = noun
            data[2] = verb
            run_instructions(data)
            if data[0] == 19690720:
                print(100 * noun + verb)
                sys.exit()
