import itertools
import re


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [{'instruction': x, 'argument': y} for (x, y) in [line.split(' = ') for line in f.read().splitlines()]]


def parse_mask(mask):
    tmp = {}
    for i in range(len(mask)):
        if mask[i] != 'X':
            tmp[i] = mask[i]
    return tmp


def part1(file='input_test.txt'):
    input_data = get_input(file)
    mem = {}
    for line in input_data:
        if line['instruction'] == 'mask':
            # set mask
            mask = parse_mask(line['argument'])
        else:
            address = re.search('[0-9]+', line['instruction']).group(0)
            binary = list('{0:036b}'.format(int(line['argument'])))

            for key, value in mask.items():
                binary[key] = value

            mem[address] = int(''.join(binary), 2)

    solution = sum(mem.values())

    print('Part 1: Solution {}'.format(solution))


def mask_address(address, mask):
    result = {}
    for i in range(len(mask)):
        if mask[i] == '0':
            result[i] = address[i]
        elif mask[i] == '1':
            result[i] = '1'
        else:
            result[i] = 'X'

    return ''.join(result.values())


def get_addresses(mask):
    addresses = []
    mask = list(mask)
    indices = [i for i, bit in enumerate(mask) if bit == 'X']
    for perm in itertools.product('01', repeat=len(indices)):
        for i, char in zip(indices, perm):
            mask[i] = char

        addresses.append(int(''.join(mask), 2))
    return addresses


def part2(file='input_test.txt'):
    input_data = get_input(file)
    mem = {}
    for line in input_data:
        if line['instruction'] == 'mask':
            # set mask
            mask = line['argument']
        else:
            address = re.search('[0-9]+', line['instruction']).group(0)
            binary_address = list('{0:036b}'.format(int(address)))
            masked_address = mask_address(binary_address, list(mask))

            for write_address in get_addresses(masked_address):
                mem[write_address] = int(line['argument'])

    solution = sum(mem.values())

    print('Part 2: Solution {}'.format(solution))


part1('input.txt')
part2('input.txt')
