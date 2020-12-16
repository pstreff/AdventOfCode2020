

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return f.read()


def process_input(file='input_test.txt'):
    input_data = get_input(file)

    rules, my_ticket, nearby_tickets = input_data.split(('\n\n'))

    processed_rules = {}

    for rule in rules.splitlines():
        name, args = rule.split(': ')
        tmp = [[int(x) for x in x.split('-')] for x in args.split(' or ')]
        processed_rules[name] = {'low': tmp[0], 'high': tmp[1]}

    processed_my_ticket = [int(x) for x in my_ticket.splitlines()[1].split(',')]

    processed_nearby_tickets = []

    for ticket in nearby_tickets.splitlines()[1:]:
        processed_nearby_tickets.append([int(x) for x in ticket.split(',')])

    return processed_rules, processed_my_ticket, processed_nearby_tickets


def valid(rules, value):
    for rule in rules.values():
        if rule['low'][0] <= value <= rule['low'][1] or rule['high'][0] <= value <= rule['high'][1]:
            return True
    else:
        return False


def part1(file='input_test.txt'):
    rules, my_ticket, nearby_tickets = process_input(file)
    count = 0

    for ticket in nearby_tickets:
        count += sum(x for x in ticket if not valid(rules, x))

    print('Part 1: Ticket scanning error rate: {}' .format(count))


def valid_for(rule, value):
    return rule['low'][0] <= value <= rule['low'][1] or rule['high'][0] <= value <= rule['high'][1]


def part2(file='input_test.txt'):
    rules, my_ticket, nearby_tickets = process_input(file)
    valid_tickets = []

    # get all valid tickets
    for ticket in nearby_tickets:
        if all(valid(rules, x) for x in ticket):
            valid_tickets.append(ticket)

    potential_fields = [set() for _ in range(len(my_ticket))]
    fields_order = ['' for _ in range(len(rules))]

    # get all potential fields for each index
    for i in range(len(my_ticket)):
        for name, rule in rules.items():
            if all(valid_for(rule, ticket[i]) for ticket in valid_tickets):
                potential_fields[i].add(name)

    # check which index has only 1 potential field
    # remove that one from each other potential fields
    # add that at the index in fields order
    while any(not field for field in fields_order):
        pos = next(pos for pos, potential_values in enumerate(potential_fields) if len(potential_values) == 1)
        value = potential_fields[pos].pop()
        for potential_values in potential_fields:
            if value in potential_values:
                potential_values.remove(value)
        fields_order[pos] = value

    departure_fields = [my_ticket[pos] for pos, field in enumerate(fields_order) if field.startswith('departure')]
    solution = 1
    for number in departure_fields:
        solution *= number
    print('Part 2: Solution {}'.format(solution))


part1('input.txt')
part2('input.txt')
