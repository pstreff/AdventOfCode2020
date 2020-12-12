

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [[i[0], int(i[1:])] for i in f.read().splitlines()]


def part1(file='input_test.txt'):
    input_data = get_input(file)
    x = 0
    y = 0
    facing = 90  # 0 = north, 90 = east, 180 = south, 270 = west

    for instruction in input_data:
        direction = instruction[0]
        argument = instruction[1]

        if direction == 'N':
            y += argument
        elif direction == 'S':
            y -= argument
        elif direction == 'E':
            x += argument
        elif direction == 'W':
            x -= argument
        elif direction == 'L':
            facing = (facing - argument) % 360
        elif direction == 'R':
            facing = (facing + argument) % 360
        elif direction == 'F':
            if facing == 0:
                # north
                y += argument
            elif facing == 90:
                # east
                x += argument
            elif facing == 180:
                # south
                y -= argument
            elif facing == 270:
                # west
                x -= argument

    manhattan_distance = abs(x) + abs(y)

    print('Part 1: Manhattan distance: {}'.format(manhattan_distance))


def part2(file='input_test.txt'):
    input_data = get_input(file)
    waypoint_x = 10
    waypoint_y = 1
    ship_x = 0
    ship_y = 0

    for instruction in input_data:
        action = instruction[0]
        argument = instruction[1]
        if action == 'N':
            waypoint_y += argument
        elif action == 'S':
            waypoint_y -= argument
        elif action == 'E':
            waypoint_x += argument
        elif action == 'W':
            waypoint_x -= argument
        elif action == 'L':
            # Rotation rules: counter-clock wise (L)
            # 90 -> x,y -> -y,x
            # 180 -> x,y -> -x,-y
            # 270 -> x,y -> y, -x
            if argument % 360 == 90:
                tmp = waypoint_x
                waypoint_x = -waypoint_y
                waypoint_y = tmp
            elif argument % 360 == 180:
                waypoint_x = -waypoint_x
                waypoint_y = -waypoint_y
            elif argument % 360 == 270:
                tmp = waypoint_x
                waypoint_x = waypoint_y
                waypoint_y = -tmp
        elif action == 'R':
            # Rotation rules: clock wise (R)
            # 90 -> x,y -> y,-x
            # 180 -> x,y -> -x,-y
            # 270 -> x,y -> -y, x
            if argument % 360 == 90:
                tmp = waypoint_x
                waypoint_x = waypoint_y
                waypoint_y = -tmp
            elif argument % 360 == 180:
                waypoint_x = -waypoint_x
                waypoint_y = -waypoint_y
            elif argument % 360 == 270:
                tmp = waypoint_x
                waypoint_x = -waypoint_y
                waypoint_y = tmp
        elif action == 'F':
            ship_x += argument * waypoint_x
            ship_y += argument * waypoint_y

    manhattan_distance = abs(ship_x) + abs(ship_y)

    print('Part 2: Manhattan distance: {}'.format(manhattan_distance))


part1('input.txt')
part2('input.txt')
