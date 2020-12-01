

with open('input.txt', 'r') as f:
    input_data = [int(line) for line in f.read().splitlines()]

for i, first in enumerate(input_data):
    for j, second in enumerate(input_data):
        if j == i:
            pass
        if first + second == 2020:
            print('First: {} Second: {}'.format(first, second))
            print('Multiplied: {}'.format(first*second))
            exit(0)
