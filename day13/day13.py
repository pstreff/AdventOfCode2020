

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read().splitlines()


def process_input(file='input_test.txt'):
    input_data = get_input(file)
    timestamp = int(input_data[0])
    bus_lines = [int(i) for i in input_data[1].split(',') if i != 'x']
    return timestamp, bus_lines


def part1(file='input_test.txt'):
    timestamp, bus_lines = process_input(file)
    bus_departures = {}

    for bus in bus_lines:
        i = int(timestamp / bus)
        departure = bus * i
        while departure < timestamp:
            i += 1
            departure = bus * i

        bus_departures[bus] = departure

    bus_to_take = min(bus_departures, key=bus_departures.get)
    waiting_time = bus_departures[bus_to_take] - timestamp
    solution = bus_to_take * waiting_time
    print('Part 1: Solution {}'.format(solution))


def process_input_part2(file='input_test.txt'):
    input_data = get_input(file)
    bus_lines = {}
    data = input_data[1].split(',')
    for i in range(len(data)):
        if data[i] == 'x':
            continue

        bus_lines[i] = int(data[i])

    return bus_lines


def part2(file='input_test.txt'):
    from sympy.ntheory.modular import crt
    bus_lines = process_input_part2(file)
    busses = []
    remainders = []

    for offset, bus_id in bus_lines.items():
        busses.append(bus_id)
        remainders.append(bus_id - offset)

    crt = crt(busses, remainders)
    print('Part 2: Solution: {}'.format(crt[0]))


part1('input.txt')
part2('input.txt')
