from functools import reduce


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [list(line.replace(' ', '')) for line in f.read().splitlines()]


def calc(equation):
    tmp = 0
    op = '+'
    while equation:
        term = equation.pop(0)
        if term == '(':
            term = calc(equation)
            if op == '+':
                tmp += int(term)
            elif op == '*':
                tmp *= int(term)
        elif term == ')':
            return tmp
        elif term == '+' or term == '*':
            op = term
        else:
            if op == '+':
                tmp += int(term)
            elif op == '*':
                tmp *= int(term)

    return tmp


def part1(file='input_test.txt'):
    input_data = get_input(file)

    solution = 0
    for eq in input_data:
        solution += calc(eq)

    print('Part 1: Solution {}'.format(solution))


def calc_part2(equation):
    reduced_list = []
    tmp = 0
    op = '+'

    while equation:
        term = equation.pop(0)

        if term == '(':
            term = calc_part2(equation)
            if op == '+':
                tmp += int(term)
            elif op == '*':
                tmp = int(term)
        elif term == ')':
            reduced_list.append(int(tmp))
            return reduce((lambda x, y: x * y), reduced_list)
        elif term == '*':
            reduced_list.append(int(tmp))
            op = term
        elif term == '+':
            op = term
        else:
            # number
            if op == '+':
                tmp += int(term)
            elif op == '*':
                tmp = int(term)

    reduced_list.append(tmp)
    return reduce((lambda x, y: x * y), reduced_list)


def part2(file='input_test.txt'):
    input_data = get_input(file)
    solution = 0
    for eq in input_data:
        solution += calc_part2(eq)

    print('Part 2: Solution {}'.format(solution))


part1('input.txt')
part2('input.txt')
