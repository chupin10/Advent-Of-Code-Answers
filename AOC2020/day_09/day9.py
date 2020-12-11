from AOC2020.helpers import GIT_DIR


def open_input() -> list[tuple[int, str]]:
    def parse_str(_s):
        return [int(v) for v in _s.strip().split('\n')]

    with open(f'{GIT_DIR}/day_09/input.txt', 'r') as fh:
        inp = fh.read()
    return parse_str(inp)


def has_pair(index: int, numbers: list[int], pream: int) -> bool:
    val = numbers[index]
    options = numbers[index-pream:index]
    for idx, v1 in enumerate(numbers[index-pream:index]):
        for v2 in options[:idx] + options[idx+1:]:
            found = v1 + v2 == val
            if found:
                return True
    return False


def find_bad_val(numbers: list[int], pream: int) -> int:
    out = None
    first_found = False
    for idx, d in enumerate(numbers[pream:]):
        valid = has_pair(idx + pream, data, pream)
        print(f'{data[idx+pream]} pair:{valid}')
        if not valid and not first_found:
            out = d
            first_found = True
    return out


def part2(bv: int, numbers: list[int]):
    for idx, _ in enumerate(numbers):
        for endpt in range(idx, len(numbers) - 1):
            subset = numbers[idx:endpt+1]
            if sum(subset) == bv:
                return min(subset), max(subset)


if __name__ == '__main__':
    data = open_input()
    bad_val = find_bad_val(data, 25)
    print(part2(bad_val, data))
