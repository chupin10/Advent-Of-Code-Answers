from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, unique

from AOC2020.helpers import GIT_DIR


def open_input():
    with open(f'{GIT_DIR}/day_05/input.txt', 'r') as fh:
        return [line.strip() for line in fh]


@unique
class SeatGroup(Enum):
    Front = 'F'
    Back = 'B'
    Left = 'L'
    Right = 'R'


def bisect(chars: str, low: int, high: int, grpA: SeatGroup, grpB: SeatGroup) -> int:
    _h = high
    _l = low

    def get_range():
        return _h - _l

    for char in chars:
        if SeatGroup(char) == grpA:
            _h -= (get_range() // 2)
        else:
            _l += (get_range() // 2)
    return _l if SeatGroup(chars[-1]) == grpB else _l


def get_row(chars: str) -> int:
    _chars = chars[:7]
    _high = 128
    _low = 0
    return bisect(_chars, _low, _high, SeatGroup.Front, SeatGroup.Back)


def get_col(chars: str) -> int:
    _chars = chars[-3:]
    _high = 8
    _low = 0
    return bisect(_chars, _low, _high, SeatGroup.Left, SeatGroup.Right)


def get_seat(chars: str) -> tuple[int, int]:
    return (get_row(chars), get_col(chars))


@dataclass
class Seat:
    row: int
    col: int
    sid: int

    @classmethod
    def from_string(cls, s: str) -> Seat:
        row, col = get_seat(s)
        sid = row * 8 + col
        return cls(row=row, col=col, sid=sid)


def maxsid(seats: list[Seat]) -> Seat:
    return max(seats, key=lambda s: s.sid)


def minsid(seats: list[Seat]) -> Seat:
    return min(seats, key=lambda s: s.sid)


def test():
    assert get_row('FBFBBFFRLR') == 44
    assert get_col('FBFBBFFRLR') == 5
    assert get_seat('FBFBBFFRLR') == (44, 5)
    tests = [
        ('FBFBBFFRLR', 357),
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
    ]
    seats = []
    for t, sid in tests:
        seat = Seat.from_string(t)
        seats.append(seat)
        assert seat.sid == sid, f'{seat} != {sid}'
    assert maxsid(seats).sid == 820, f'{maxsid(seats)}'


if __name__ == '__main__':
    test()
    seats = [Seat.from_string(entry) for entry in open_input()]
    print(maxsid(seats))
    mins = minsid(seats)
    maxs = maxsid(seats)
    all_seats = set(range(mins.sid + 1, maxs.sid))
    print(all_seats - set([seat.sid for seat in seats]))
