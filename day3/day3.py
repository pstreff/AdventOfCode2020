

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def part1(file='input_test.txt'):
    # formel: (index * slope) % base_width
    slope = 3
    map = get_input(file)
    map_base_width = len(map[0])
    trees = 0
    for i in range(0, len(map)):
        index_at_check = (i * slope) % map_base_width
        if map[i][index_at_check] == '#':
            trees += 1

    print('Part 1: Number of trees encountered: {}'.format(trees))


def part2(file='input_test.txt'):
    import numpy as np

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    encounters = []
    map = get_input(file)
    map_base_width = len(map[0])
    for slope in slopes:
        right_slope = slope[0]
        down_slope = slope[1]

        trees = 0
        for i in range(0, len(map), down_slope):
            index_at_check = (int((i * right_slope) / down_slope)) % map_base_width
            if map[i][index_at_check] == '#':
                trees += 1

        encounters.append(trees)

    print('Part 2: Encounters multiplied: {}'.format(np.prod(encounters)))


part1('input.txt')
part2('input.txt')

