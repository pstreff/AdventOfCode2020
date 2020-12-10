

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [int(line) for line in f.read().splitlines()]


def part1(file='input_test.txt'):
    input_data = get_input(file)
    input_data.append(0)
    input_data.sort()
    jolt_differences = {
        1: 0,
        2: 0,
        3: 0
    }

    for index in range(len(input_data)):
        try:
            difference = input_data[index + 1] - input_data[index]
        except IndexError:
            difference = 3

        jolt_differences[difference] += 1

    solution = jolt_differences[1] * jolt_differences[3]

    print('Part 1: Solution: {}'.format(solution))


def part2(file='input_test.txt'):
    input_data = get_input(file)
    input_data.append(0)
    input_data.append(max(input_data) + 3)
    input_data.sort()
    cache = {}

    def calc_paths(i):
        ans = 0
        if i == len(input_data) - 1:
            return 1
        if i in cache:
            return cache[i]

        for j in range(i + 1, len(input_data)):
            if input_data[j] - input_data[i] <= 3:
                ans += calc_paths(j)
            else:
                break
        cache[i] = ans
        return ans

    solution = calc_paths(0)
    print('Part 2: Solution: {}'.format(solution))


part1('input.txt')
part2('input.txt')
