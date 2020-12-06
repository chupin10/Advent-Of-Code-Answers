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
TEST_ANSWERS = [[3, 3, 3, 1, 1], 11]


def open_input() -> list[str]:
    with open(f'{GIT_DIR}/day_06/input.txt', 'r') as fh:
        lines = fh.read()
        groups = [line.replace('\n', '') for line in lines.split('\n\n')]
        return groups


def numyes(group: str) -> int:
    return len(set(group))


if __name__ == '__main__':
    groups = [line.replace('\n', '') for line in TEST.split('\n\n')]
    yeses = []
    for group, answer in zip(groups, TEST_ANSWERS[0]):
        n = numyes(group)
        assert n == answer
        yeses.append(n)
    assert sum(yeses) == TEST_ANSWERS[1]

    groups = open_input()
    print(sum([numyes(group) for group in groups]))
