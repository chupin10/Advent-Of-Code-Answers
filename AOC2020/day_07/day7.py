from __future__ import annotations
from dataclasses import dataclass

from AOC2020.helpers import GIT_DIR


def open_input() -> list[tuple[int, str]]:
    _TEST = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    _TEST2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
    # return _TEST2.split('\n')
    with open(f'{GIT_DIR}/day_07/input.txt', 'r') as fh:
        return fh.read().split('\n')[:-1]


@dataclass
class RuleSet:
    color: str
    items: list[dict]

    def possible_contents(self) -> set:
        if len(self.items) == 1 and self.items[0] == {}:
            return set()
        out = set()
        for item in self.items:
            out.add(item['color'])
            out |= ALL_RULES[item['color']].possible_contents()
        return out

    def min_contents(self) -> int:
        if len(self.items) == 1 and self.items[0] == {}:
            return 0
        out = 0
        for item in self.items:
            out += item['num']
            out += item['num'] * ALL_RULES[item['color']].min_contents()
        return out


# cache for created rules
ALL_RULES: dict[str, RuleSet] = {}


def create_rule(line: str) -> RuleSet:
    sl = line.split(' ')
    assert sl[3] == 'contain', f'{sl}'
    col = ' '.join(sl[0:2]).replace(' ', '')
    if col in ALL_RULES.keys():
        return ALL_RULES[col]

    def get_items(_sl: tuple[str]) -> list[dict]:
        if _sl[4] == 'no':
            return [{}]
        items = '_'.join(_sl[4:])
        items = items.split(',')
        out = []
        for item in items:
            item = item.replace(',', '').replace('.', '').replace(' ', '').split('_')
            item = [it for it in item if it != '']
            _d = {
                'num': int(item[0]),
                'color': (item[1] + item[2]),
            }
            out.append(_d)
        return out

    rule = RuleSet(color=col, items=get_items(sl))
    ALL_RULES[col] = rule
    return rule


if __name__ == '__main__':
    data = open_input()
    for rule in data:
        create_rule(rule)
    count = 0
    for color, rule in ALL_RULES.items():
        if 'shinygold' in rule.possible_contents():
            count += 1
    print(count)
    print(ALL_RULES['shinygold'].min_contents())


