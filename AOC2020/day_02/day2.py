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


def is_valid_partA(key: str, lims: tuple[int, int], chars: str) -> bool:
    count = chars.count(key)
    return lims[0] <= count <= lims[1]


def is_valid_partB(key: str, lims: tuple[int, int], chars: str) -> bool:
    print(lims)
    if key == chars[lims[0] - 1] and key != chars[lims[1] - 1]:
        return True
    if key == chars[lims[1] - 1] and key != chars[lims[0] - 1]:
        return True
    else:
        return False


if __name__ == '__main__':
    lines = open_input()
    # lines = TEST_CASES
    validity = [None]*len(lines)
    for i, test in enumerate(lines):
        out = get_vals(test)
        if is_valid_partB(*out):
            validity[i] = 1
        else:
            validity[i] = 0
    print(f'Found {len(validity)} passwords. {sum(validity)} are valid')
