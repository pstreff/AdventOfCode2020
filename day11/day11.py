import copy


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [list(i) for i in f.read().splitlines()]


def part1(file='input_test.txt'):
    seat_map = get_input(file)
    new_map = get_input(file)

    directions = [
        [-1, -1],
        [0, -1],
        [+1, -1],
        [-1, 0],
        [+1, 0],
        [-1, +1],
        [0, +1],
        [+1, +1],
    ]

    while True:
        for y in range(len(seat_map)):
            for x in range(len(seat_map[0])):
                if seat_map[y][x] == '.':
                    new_map[y][x] = '.'
                    continue

                occupied = 0
                for direction in directions:
                    check_y = y + direction[1]
                    check_x = x + direction[0]

                    if check_y < 0 or check_y >= len(seat_map) or check_x < 0 or check_x >= len(seat_map[0]):
                        continue

                    seat = seat_map[y + direction[1]][x + direction[0]]

                    if seat == '#':
                        occupied += 1

                if seat_map[y][x] == 'L' and occupied == 0:
                    new_map[y][x] = '#'
                elif seat_map[y][x] == '#' and occupied >= 4:
                    new_map[y][x] = 'L'
                else:
                    new_map[y][x] = seat_map[y][x]

        if new_map == seat_map:
            break

        seat_map = copy.deepcopy(new_map)

    total_occupied = sum([row.count('#') for row in seat_map])

    print('Part 1: Total occupied places: {}'.format(total_occupied))


cache = {}


def find_first_visible_seat(seat_map, x, y, x_dir, y_dir):
    # go into the direction given until we find a seat (free or occupied)
    check_y = y
    check_x = x

    while True:
        check_y += y_dir
        check_x += x_dir

        if check_y < 0 or check_y >= len(seat_map) or check_x < 0 or check_x >= len(seat_map[0]):
            return 'L'  # out of bounds so not occupied, setting as a free seat

        check_seat = seat_map[check_y][check_x]

        if check_seat == 'L' or check_seat == '#':
            return check_seat


def part2(file='input_test.txt'):
    seat_map = get_input(file)
    new_map = get_input(file)

    directions = [
        [-1, -1],
        [0, -1],
        [+1, -1],
        [-1, 0],
        [+1, 0],
        [-1, +1],
        [0, +1],
        [+1, +1],
    ]

    while True:
        for y in range(len(seat_map)):
            for x in range(len(seat_map[0])):
                if seat_map[y][x] == '.':
                    new_map[y][x] = '.'
                    continue

                occupied = 0
                for direction in directions:

                    first_visible_seat = find_first_visible_seat(seat_map, x, y, direction[0], direction[1])

                    if first_visible_seat == '#':
                        occupied += 1

                if seat_map[y][x] == 'L' and occupied == 0:
                    new_map[y][x] = '#'
                elif seat_map[y][x] == '#' and occupied >= 5:
                    new_map[y][x] = 'L'
                else:
                    new_map[y][x] = seat_map[y][x]

        if new_map == seat_map:
            break

        seat_map = copy.deepcopy(new_map)

    total_occupied = sum([row.count('#') for row in seat_map])

    print('Part 2: Total occupied places: {}'.format(total_occupied))


part1('input.txt')
part2('input.txt')
