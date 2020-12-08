

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def part1(file='input_test.txt'):
    input_data = get_input(file)
    accumulator = 0
    visited_indexes = []
    current_index = 0
    infinite_loop = False

    while not infinite_loop:
        if current_index in visited_indexes:
            infinite_loop = True
            continue
        else:
            visited_indexes.append(current_index)

        operation, argument = input_data[current_index].split(' ')

        if operation == 'nop':
            current_index += 1
        elif operation == 'acc':
            current_index += 1
            accumulator += int(argument)
        elif operation == 'jmp':
            current_index += int(argument)

    print('Part 1: Accumulator before the infinite loop: {}'.format(accumulator))


def check_execution(commands, accumulator, visited_indexes, current_index, patch_list=False):
    while True:
        if current_index in visited_indexes:
            return None
        elif current_index >= len(commands):
            break
        else:
            visited_indexes.append(current_index)

        operation, argument = commands[current_index].split(' ')
        if operation == 'nop':
            if patch_list:
                # if we should patch,
                # switch to jump operation and check if it solves
                # if not continue normally
                patched_list = commands.copy()
                patched_list[current_index] = 'jmp ' + argument

                check = check_execution(patched_list, accumulator, visited_indexes.copy()[:-1], current_index)
                if check:
                    # check returned value so this change was correct
                    accumulator = check
                    break
            current_index += 1
        elif operation == 'acc':
            current_index += 1
            accumulator += int(argument)
        elif operation == 'jmp':
            if patch_list:
                # if we should patch,
                # switch to nop operation and check if it solves
                # if not continue normally
                patched_list = commands.copy()
                patched_list[current_index] = 'nop ' + argument

                check = check_execution(patched_list, accumulator, visited_indexes.copy()[:-1], current_index)
                if check:
                    # check returned value so this change was correct
                    accumulator = check
                    break
            current_index += int(argument)

    return accumulator


def part2(file='input_test.txt'):
    input_data = get_input(file)
    accumulator = check_execution(input_data, 0, [], 0, True)
    print('Part 2: Accumulator at finished program: {}'.format(accumulator))


part1('input.txt')
part2('input.txt')
