from AOC2020.helpers import GIT_DIR

TEST = """abc

a
b
c

ab
ac

a
a
a
a

b"""
TEST_ANSWERS_1 = [[3, 3, 3, 1, 1], 11]
TEST_ANSWERS_2 = [[3, 0, 1, 1, 1], 6]


def open_input() -> list[tuple[int, str]]:
    # NOTE: you need to have 2 blank lines at the end of input.txt
    with open(f'{GIT_DIR}/day_06/input.txt', 'r') as fh:
        lines = fh.read()
        groups = [(line.count('\n') + 1, line.replace('\n', ''))
                  for line in lines.split('\n\n')]
        return groups


def numyes(_group: str) -> int:
    return len(set(_group))


def num_unanimous(_group: str, grpsz: int) -> int:
    if grpsz == 1:
        return len(set(_group))
    un = 0
    for char in set(_group):
        if _group.count(char) == grpsz:
            un += 1
    return un


if __name__ == '__main__':
    groups = [(line.count('\n') + 1, line.replace('\n', ''))
              for line in TEST.split('\n\n')]
    yeses = []
    for (groupsize, group), answer in zip(groups, TEST_ANSWERS_2[0]):
        n = num_unanimous(group, groupsize)
        assert n == answer, f'{n=}\t{answer=}'
        yeses.append(n)
    assert sum(yeses) == TEST_ANSWERS_2[1]

    groups = open_input()
    print(sum([num_unanimous(group, groupsize) for (groupsize, group) in groups]))
