import itertools

import numpy as np

with open('input.txt', 'r') as f:
    input_data = [int(line) for line in f.read().splitlines()]


for i in itertools.combinations(input_data, 3):
    if sum(i) == 2020:
        print('Tuple: {}'.format(i))
        print('Multiplied: {}'.format(np.prod(i)))
