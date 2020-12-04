import re


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def process_input(file='input_test.txt'):
    input_list = get_input(file)
    processed = []
    tmp = {}
    input_list.append('')
    for line in input_list:
        if line == '':
            processed.append(tmp)
            tmp = {}
        else:
            for i in line.split():
                key, value = i.split(':')
                tmp[key] = value

    return processed


def valid_passport_part_1(passport):
    checks = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for check_key in checks:
        if check_key not in passport.keys():
            return False
    return True


def check_byr(value):
    # four digits; at least 1920 and at most 2002
    return value.isdigit() and len(value) == 4 and 1920 <= int(value) <= 2002


def check_iyr(value):
    # four digits; at least 2010 and at most 2020
    return value.isdigit() and len(value) == 4 and 2010 <= int(value) <= 2020


def check_eyr(value):
    # four digits; at least 2020 and at most 2030
    return value.isdigit() and len(value) == 4 and 2020 <= int(value) <= 2030


def check_hgt(value):
    # a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193
    # If in, the number must be at least 59 and at most 76
    match = re.search('^([0-9]+)(cm|in)$', value)

    if not match:
        return False

    if match.group(2) == 'cm':
        return 150 <= int(match.group(1)) <= 193
    elif match.group(2) == 'in':
        return 59 <= int(match.group(1)) <= 76


def check_hcl(value):
    # a # followed by exactly six characters 0-9 or a-f
    return bool(re.search('^#[0-9a-f]{6}$', value))


def check_ecl(value):
    # exactly one of: amb blu brn gry grn hzl oth
    allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in allowed


def check_pid(value):
    # a nine-digit number, including leading zeroes.
    return bool(re.search('^[0-9]{9}$', value))


def valid_passport(passport):
    checks = {
        'byr': check_byr,
        'iyr': check_iyr,
        'eyr': check_eyr,
        'hgt': check_hgt,
        'hcl': check_hcl,
        'ecl': check_ecl,
        'pid': check_pid
    }
    for check_key, check_method in checks.items():
        if check_key not in passport.keys():
            return False
        else:
            if not check_method(passport[check_key]):
                return False
    return True


def part1(file='input_test.txt'):
    count = 0
    for passport in process_input(file):
        if valid_passport_part_1(passport):
            count += 1

    print('Part 1: Total number of valid passports: {}'.format(count))


def part2(file='input_test.txt'):
    count = 0
    for passport in process_input(file):
        if valid_passport(passport):
            count += 1

    print('Part 2: Total number of valid passports: {}'.format(count))


part1('input.txt')
part2('input.txt')
