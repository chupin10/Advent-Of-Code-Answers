from math import floor
from typing import List, Tuple
import time

CACHE = {}


def open_input() -> List[float]:
    with open('../inputs/day1.txt', 'r') as f:
        return [float(mass) for mass in f]


def cache_mass(mass: int, fuel: int) -> None:
    if mass not in CACHE.keys():
        CACHE[mass] = fuel


def get_fuel_required(mass: int) -> Tuple[int, bool]:
    if mass in CACHE.keys():
        return CACHE[mass], True

    total_fuel = fuel = floor(mass / 3) - 2
    if fuel <= 0:
        cache_mass(mass, fuel)
        return total_fuel, False
    else:
        while fuel > 0:
            fuel, was_cached = get_fuel_required(fuel)
            total_fuel += fuel if fuel > 0 else 0
            if was_cached:
                return total_fuel, True
        cache_mass(mass, total_fuel)
        return total_fuel, False


if __name__ == '__main__':
    t0 = time.time()
    fuelreqs = [get_fuel_required(mass)[0] for i, mass in enumerate(open_input())]
    print('Completion time', time.time() - t0)
    print('Part 2 answer:', sum(fuelreqs))
    print('14:', get_fuel_required(14)[0], 'vs 2')
    print('1969:', get_fuel_required(1969)[0], 'vs 966')
    print('100756:', get_fuel_required(100756)[0], 'vs 50346')
