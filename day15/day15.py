

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().split(',')


def part1(file='input_test.txt'):
    input_data = get_input(file)
    memory = {}
    input_length = len(input_data)

    # game loop
    for turn in range(1, 2021):
        if turn <= input_length:
            last_number = int(input_data.pop(0))
            memory[last_number] = turn
            continue
        if last_number not in memory or memory[last_number] == turn - 1:
            # number has not been spoken before
            memory[last_number] = turn - 1
            last_number = 0
        else:
            # the next number to speak is the difference between the turn number when it was last spoken
            last_time_spoken = memory[last_number]
            memory[last_number] = turn - 1
            last_number = turn - 1 - last_time_spoken

    print('2020th number {}'.format(last_number))


def part2(file='input_test.txt'):
    input_data = get_input(file)
    memory = {}
    input_length = len(input_data)

    # game loop
    for turn in range(1, 30000001):
        if turn <= input_length:
            last_number = int(input_data.pop(0))
            memory[last_number] = turn
            continue
        if last_number not in memory or memory[last_number] == turn - 1:
            # number has not been spoken before
            memory[last_number] = turn - 1
            last_number = 0
        else:
            # the next number to speak is the difference between the turn number when it was last spoken
            last_time_spoken = memory[last_number]
            memory[last_number] = turn - 1
            last_number = turn - 1 - last_time_spoken

    print('30000000th number {}'.format(last_number))


part1('input.txt')
part2('input.txt')
