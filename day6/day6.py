

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def process_input(file='input_test.txt'):
    input_list = get_input(file)
    processed = []
    input_list.append('')
    tmp = []
    for line in input_list:
        if line == '':
            processed.append(tmp)
            tmp = []
        else:
            for i in line.split():
                tmp += [char for char in i if char not in tmp]

    return processed


def part1(file='input_test.txt'):
    input_data = process_input(file)

    sum_count = sum([len(group) for group in input_data])

    print('Part 1: Sum of counts: {}'.format(sum_count))


def process_input_part_2(file='input_test.txt'):
    input_list = get_input(file)
    processed = []
    input_list.append('')
    tmp = {}
    persons_in_group = 0
    for line in input_list:
        if line == '':
            processed.append({
                'person_count': persons_in_group,
                'questions': tmp
            })
            tmp = {}
            persons_in_group = 0
        else:
            for i in line.split():
                for char in i:
                    tmp[char] = tmp.get(char, 0) + 1

            persons_in_group += 1

    return processed


def part2(file='input_test.txt'):
    data = process_input_part_2(file)
    sum_count = 0
    for group in data:
        for value in group['questions'].values():
            if value == group['person_count']:
                sum_count += 1
    print('Part 2: {}'.format(sum_count))


part1('input.txt')
part2('input.txt')
