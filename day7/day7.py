import re


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def process_input(file='input_test.txt'):
    input_data = get_input(file)
    processed = {}
    for definition in input_data:
        tmp = definition.split(' bags contain ')
        tmp_list = []
        for x in tmp[1].split(', '):
            tmp_list.append(re.sub(' bag[s]?[.]?', '', x))

        processed[tmp[0]] = tmp_list

    return processed


def part1(file='input_test.txt'):
    input_data = process_input(file)

    search_colors = ['shiny gold']
    possible_bags = []
    while search_colors:
        search_color = search_colors.pop()

        for bag, contents in input_data.items():
            if bag in possible_bags:
                continue
            if any(search_color in content for content in contents):
                search_colors.append(bag)
                possible_bags.append(bag)

    print('Part 1: Number of possible bags: {}'.format(len(possible_bags)))


def resolve_bag_list(bag_list, input_data):
    # recursive
    if 'no other' in bag_list:
        return 0

    bag_count = 0
    for bag in bag_list:
        number, color = bag.split(' ', maxsplit=1)
        recur = resolve_bag_list(input_data[color], input_data)
        bag_count += int(number) + (int(number) * recur)

    return bag_count


def part2(file='input_test.txt'):
    input_data = process_input(file)
    required_number = resolve_bag_list(input_data['shiny gold'], input_data)
    print('Part 2: Total bags required: {}'.format(required_number))
    pass


part1('input.txt')
part2('input.txt')
