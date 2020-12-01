import itertools

import numpy as np

with open('input.txt', 'r') as f:
    input_data = [int(line) for line in f.read().splitlines()]


# Solution with itertools

for i in itertools.combinations(input_data, 2):
    if sum(i) == 2020:
        print('First: {} Second: {}'.format(i[0], i[1]))
        print('Multiplied: {}'.format(np.prod(i)))


# First solution
# for i, first in enumerate(input_data):
#     for j, second in enumerate(input_data):
#         if j == i:
#             pass
#         if first + second == 2020:
#             print('First: {} Second: {}'.format(first, second))
#             print('Multiplied: {}'.format(first*second))
#             exit(0)
