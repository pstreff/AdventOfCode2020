

def process_input(data):
    rule, char, password = data

    rule = [int(line) for line in rule.split('-')]
    char = char.replace(':', '')

    return rule, char, password


def part1(input_file='input_test.txt'):
    with open(input_file, 'r') as f:
        input_data = [line.split(' ') for line in f.read().splitlines()]

    count = 0
    for line in input_data:
        rule, char, password = process_input(line)

        if rule[0] <= password.count(char) <= rule[1]:
            count += 1

    print('Part 1: {} valid passwords'.format(count))


def part2(input_file='input_test.txt'):
    with open(input_file, 'r') as f:
        input_data = [line.split(' ') for line in f.read().splitlines()]

    count = 0
    for line in input_data:
        rule, char, password = process_input(line)

        if (password[rule[0] -1] == char) ^ (password[rule[1] -1] == char):
            count += 1

    print('Part 2: {} valid passwords'.format(count))


part1('input1.txt')
part2('input1.txt')