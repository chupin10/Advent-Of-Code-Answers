from __future__ import annotations
from dataclasses import dataclass

from AOC2020.helpers import GIT_DIR


def parse_str(_s) -> list[int]:
    return [int(v) for v in _s.strip().split('\n')]


def open_input() -> list[int]:

    test_inp1 = """16
10
15
5
1
11
7
19
6
12
4"""
    test_inp2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

    with open(f'{GIT_DIR}/day_10/input.txt', 'r') as fh:
        inp = fh.read()
    return parse_str(inp)


@dataclass
class Adaptor:
    rating: int
    in_use: bool = False

    @property
    def valid_inputs(self) -> set[int]:
        return set(range(self.rating - 3, self.rating + 1))

    # implement operators for use with max/min calls
    # == and != implemented for free from dataclass wrapper
    def __ge__(self, other: Adaptor) -> bool:
        return self.rating >= other.rating

    def __gt__(self, other: Adaptor) -> bool:
        return self.rating > other.rating

    def __le__(self, other: Adaptor) -> bool:
        return self.rating <= other.rating

    def __lt__(self, other: Adaptor) -> bool:
        return self.rating < other.rating

    def __bool__(self):
        return self.in_use


def get_all_adaptors(vals: list[int]) -> list[Adaptor]:
    return [Adaptor(val) for val in vals]


def get_device_rating(adaptors: list[Adaptor]) -> int:
    return max(adaptors).rating + 3


def valid_adaptor_ratings(input_jolt: int) -> list[int]:
    return list(range(input_jolt + 1, input_jolt + 4))


def update_diffs(diffs: dict, diff: int) -> None:
    if diff in diffs.keys():
        diffs[diff] += 1
    else:
        diffs[diff] = 1


def find_next_adaptor(ratings: list[int], adaptors: list[Adaptor]) -> Adaptor:
    for rating in ratings:
        mock_adap = Adaptor(rating, False)  # guarantees we don't grab in-use adaptors
        if mock_adap in adaptors:
            ad = adaptors[adaptors.index(mock_adap)]
            return ad


def connect_adaptors(adaptors: list[Adaptor]) -> dict:
    diffs = {}
    input_jolt = 0
    while not all(adaptors):
        adaptor_ratings = valid_adaptor_ratings(input_jolt)
        cur_ad = find_next_adaptor(adaptor_ratings, adaptors)
        cur_ad.in_use = True
        diff = cur_ad.rating - input_jolt
        update_diffs(diffs, diff)
        input_jolt = cur_ad.rating
    return diffs


def get_all_paths(adaptors: list[int]) -> int:
    paths = {0: 1}
    for ad in adaptors:
        for j_diff in range(1, 4):
            if ad.rating not in paths.keys():
                paths[ad.rating] = 0
            paths[ad.rating] += paths.get(ad.rating - j_diff, 0)
    return paths[adaptors[-1].rating]


if __name__ == '__main__':
    my_adaptors = get_all_adaptors(open_input())
    mydev = Adaptor(get_device_rating(my_adaptors), False)
    my_adaptors.append(mydev)
    print(max(my_adaptors) == max(my_adaptors))
    diffsfound = connect_adaptors(my_adaptors)
    print(diffsfound[1] * diffsfound[3])
    print(get_all_paths(sorted(my_adaptors)))
