from AOC2020.helpers import GIT_DIR


def open_input() -> list[int]:
    with open(f'{GIT_DIR}/day_01/input.txt', 'r') as fh:
        return [int(line) for line in fh]


def try_combo(values: list[int]) -> bool:
    return sum(values) == 2020


def pair_to_answer(values: list[int]) -> int:
    out = values[0]
    for val in values[1:]:
        out *= val
    return out


def create_subset(v: int, values: set[int]) -> set[int]:
    subset = values.copy()
    subset.remove(v)
    return subset


if __name__ == '__main__':
    vals = open_input()
    vals = set(vals)
    invalid = set()
    for val1 in vals:
        if val1 in invalid:
            continue
        subset1 = create_subset(val1, vals)
        for val2 in subset1:
            if val2 in invalid:
                continue
            subset2 = create_subset(val2, subset1)
            for val3 in subset2:
                if val3 in invalid:
                    continue
                testset = [val1, val2, val3]
                if try_combo(testset):
                    print(pair_to_answer(testset))
                    print(testset)
        invalid.add(val1)
