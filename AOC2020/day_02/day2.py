from AOC2020.helpers import GIT_DIR


def open_input() -> list[int]:
    with open(f'{GIT_DIR}/day_02/input.txt', 'r') as fh:
        return [line.strip() for line in fh]


TEST_CASES = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]


def get_vals(line: str):
    els = line.split(' ')
    lims = els[0].split('-')
    lims = [int(el) for el in lims]
    key = els[1][0]
    chars = els[2]
    return (key, lims, chars)


def is_valid(key: str, lims: tuple[int, int], chars: str) -> bool:
    count = chars.count(key)
    return lims[0] <= count <= lims[1]


if __name__ == '__main__':
    lines = open_input()
    validity = [None]*len(lines)
    for i, test in enumerate(lines):
        out = get_vals(test)
        if is_valid(*out):
            validity[i] = 1
        else:
            validity[i] = 0
    print(f'Found {len(validity)} passwords. {sum(validity)} are valid')
