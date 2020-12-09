import itertools


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [int(line) for line in f.read().splitlines()]


def part1(file='input_test.txt'):
    input_data = get_input(file)
    preamble_length = 25
    preamble = input_data[0:preamble_length]
    input_data = input_data[preamble_length:]

    while True:
        check = input_data[0]

        sums = [sum(x) for x in itertools.combinations(preamble, 2)]

        if check not in sums:
            return check

        del input_data[0]
        del preamble[0]
        preamble.append(check)


def part2(file='input_test.txt'):
    input_data = get_input(file)
    invalid_number = part1(file)

    for first in range(len(input_data)):
        sum = input_data[first]
        for last in range(first + 1, len(input_data)):
            sum += input_data[last]

            if sum == invalid_number:
                contiguous_set = input_data[first:last+1]  # last + 1 because slicing works in mysterious ways
                return min(contiguous_set) + max(contiguous_set)


print('Part 1: {} is not the sum of 2 values!'.format(part1('input.txt')))
print('Part 2: Encryption weakness in list: {}'.format(part2('input.txt')))
