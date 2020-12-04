from functools import partial

from AOC2020.helpers import GIT_DIR


def open_input():
    with open(f'{GIT_DIR}/day_04/input.txt', 'r') as fh:
        return fh.read()


EXPECTED_FIELDS = {
    'byr': 'Birth Year',
    'iyr': 'Issue Year',
    'eyr': 'Expiration Year',
    'hgt': 'Height',
    'hcl': 'Hair Color',
    'ecl': 'Eye Color',
    'pid': 'Passport ID',
    'cid': 'Country ID',
}

ALL_FIELDS = set(EXPECTED_FIELDS.keys())
NEEDED_FIELDS = ALL_FIELDS.copy()
NEEDED_FIELDS.remove('cid')


TESTS = """hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


TEST_RES = [True, False, True, False]


def has_all_fields(passport):
    for key in NEEDED_FIELDS:
        if key not in passport.keys():
            return False
    return True


def check_year(early, late, year):
    year = int(year)
    return early <= year <= late


def check_height(lowcm, highcm, lowin, highin, val):
    try:
        value, units = int(val[:-2]), val[-2:]
    except ValueError:
        return False
    if units == 'cm':
        return lowcm <= value <= highcm
    else:
        return lowin <= value <= highin


def check_hair_color(col):
    if col[0] != '#' and len(col) != 7:
        return False
    return True


def check_eye_color(eye):
    if eye in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def check_pass_id(id):
    digits = [str(i) for i in range(10)]
    return len(id) == 9 and all([(v in digits) for v in id])


def check_cid(id):
    return True


VALIDITY_CHECKS = {
    'byr': partial(check_year, 1920, 2002),
    'iyr': partial(check_year, 2010, 2020),
    'eyr': partial(check_year, 2020, 2030),
    'hgt': partial(check_height, 150, 193, 59, 76),
    'hcl': check_hair_color,
    'ecl': check_eye_color,
    'pid': check_pass_id,
    'cid': check_cid,
}


def has_valid_data(passport):
    for field, value in passport.items():
        res = VALIDITY_CHECKS[field](value)
        if not res:
            return False
    return True


def is_valid(passport):
    return all([test(passport) for test in [has_all_fields, has_valid_data]])


def to_entry(passport):
    s = ','.join(passport)  # one string
    s = s.replace('\n', ',')
    s = s.replace(' ', ',')
    s = s.split(',')
    if s != ['']:
        entry = {
            kv.split(':')[0]: kv.split(':')[1] for kv in s
        }
        return entry


def get_passports(inp):
    all_passports = []
    current_passport = []
    for line in inp:
        if len(line) > 1:
            current_passport.append(line)
        else:
            content = to_entry(current_passport)
            if content is not None:
                all_passports.append(content)
            current_passport = []
    return all_passports


if __name__ == '__main__':
    # results = [is_valid(test) for test in get_passports(TESTS.split('\n'))]
    results = [is_valid(test) for test in get_passports(open_input().split('\n'))]
    print(results)
    print(f'Number of valid passports: {sum(results)}')
