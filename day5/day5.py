import math


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def decode_seats(file):
    input_data = get_input(file)
    seat_ids = []

    for definition in input_data:

        row_definition = definition[:-3]
        column_definition = definition[-3:]

        row_lower_limit = 0
        row_upper_limit = 127

        for char in row_definition:
            if char == 'B':
                row_lower_limit = int(math.ceil((row_upper_limit + row_lower_limit) / 2))
            elif char == 'F':
                row_upper_limit = math.floor((row_upper_limit + row_lower_limit) / 2)

        row = row_lower_limit

        column_lower_limit = 0
        column_upper_limit = 7

        for char in column_definition:
            if char == 'R':
                column_lower_limit = int(math.ceil((column_upper_limit + column_lower_limit) / 2))
            elif char == 'L':
                column_upper_limit = math.floor((column_upper_limit + column_lower_limit) / 2)
        column = column_lower_limit

        seat_ids.append(row * 8 + column)

    return seat_ids


def part1(file='input_test.txt'):
    seat_ids = decode_seats(file)

    print('Part 1: Highest Seat ID: {}'.format(max(seat_ids)))


def part2(file='input_test.txt'):
    seat_ids = decode_seats(file)
    seat_ids.sort()
    free_seat = [x for x in range(seat_ids[0], seat_ids[-1] + 1) if x not in seat_ids]
    print('Part 2: Free seat {}'.format(free_seat))


part1('input.txt')
part2('input.txt')
