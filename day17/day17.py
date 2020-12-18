import copy
import itertools

import numpy as np


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [list(map(lambda x: 1 if x == '#' else 0, line)) for line in f.read().splitlines()]


def pad_grid(grid, dimensions=3):
    return np.pad(grid, [(1,1) for _ in range(dimensions)], mode='constant', constant_values=0)


def check_neighbours(grid, x, y, z, w=0, dimensions=3):
    directions = list(itertools.product([-1, 0, 1], repeat=dimensions))
    directions.remove((0,) * dimensions)
    count = 0
    for direction in directions:
        try:
            if dimensions == 4:
                if grid[w + direction[3]][z + direction[2]][y + direction[1]][x + direction[0]] == 1:
                    count += 1
            else:
                if grid[z + direction[2]][y + direction[1]][x + direction[0]] == 1:
                    count += 1
        except IndexError:
            continue

    return count


def part1(file='input_test.txt'):
    input_data = get_input(file)

    grid = np.zeros((1, len(input_data), len(input_data)), dtype=int)
    grid[0] = copy.deepcopy(input_data)

    for _ in range(6):
        grid = pad_grid(grid)
        new_grid = np.zeros((len(grid), len(grid[0]), len(grid[0][0])), dtype=int)

        for z in range(len(grid)):
            for y in range(len(grid[z])):
                for x in range(len(grid[z][y])):
                    active_neighbours = check_neighbours(grid, x, y, z)
                    current_cube = grid[z][y][x]
                    new = 1 if (current_cube == 1 and 2 <= active_neighbours <= 3) or (current_cube == 0 and active_neighbours == 3) else 0
                    new_grid[z][y][x] = new

        grid = copy.deepcopy(new_grid)

    solution = np.sum(grid)
    print('Part 1: Active cubes {}'.format(solution))


def part2(file='input_test.txt'):
    input_data = get_input(file)

    grid = np.zeros((1, 1, len(input_data), len(input_data)), dtype=int)
    grid[0][0] = copy.deepcopy(input_data)

    for _ in range(6):
        grid = pad_grid(grid, dimensions=4)
        new_grid = np.zeros((len(grid), len(grid[0]), len(grid[0][0]), len(grid[0][0][0])), dtype=int)

        for w in range(len(grid)):
            for z in range(len(grid[w])):
                for y in range(len(grid[w][z])):
                    for x in range(len(grid[w][z][y])):
                        active_neighbours = check_neighbours(grid, x, y, z, w, dimensions=4)
                        current_cube = grid[w][z][y][x]
                        new = 1 if (current_cube == 1 and 2 <= active_neighbours <= 3) or (
                                    current_cube == 0 and active_neighbours == 3) else 0
                        new_grid[w][z][y][x] = new

        grid = copy.deepcopy(new_grid)

    solution = np.sum(grid)
    print('Part 2: Active cubes {}'.format(solution))


part1('input.txt')
part2('input.txt')
