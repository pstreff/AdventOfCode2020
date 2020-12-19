from pyformlang.cfg import Variable, Production, Terminal, CFG


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        data = f.read()
        rules, messages = data.split(('\n\n'))
        rules = {x: y for (x, y) in [line.split(': ') for line in rules.splitlines()]}
        messages = [x for x in messages.splitlines()]

        return rules, messages


def part1(file='input_test.txt'):
    rules, messages = get_input(file)

    rule_variables = set()
    rule_products = set()

    for rule in rules:
        subs = rules[rule].split(' | ')
        rule_variables.add(Variable(rule))
        for sub in subs:
            if sub == '"a"' or sub == '"b"':
                rule_products.add(Production(Variable(rule), [Terminal(sub.replace('"', ''))]))
            else:
                rule_products.add(Production(Variable(rule), [Variable(x) for x in sub.split(' ')]))

    cfg = CFG(rule_variables, {Terminal('a'), Terminal('b')}, Variable('0'), rule_products)
    count = 0

    for message in messages:
        if cfg.contains(message):
            count += 1

    print('Part 1: Solution {}'.format(count))


def part2(file='input_test.txt'):
    rules, messages = get_input(file)

    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    rule_variables = set()
    rule_products = set()

    for rule in rules:
        subs = rules[rule].split(' | ')
        rule_variables.add(Variable(rule))
        for sub in subs:
            if sub == '"a"' or sub == '"b"':
                rule_products.add(Production(Variable(rule), [Terminal(sub.replace('"', ''))]))
            else:
                rule_products.add(Production(Variable(rule), [Variable(x) for x in sub.split(' ')]))

    cfg = CFG(rule_variables, {Terminal('a'), Terminal('b')}, Variable('0'), rule_products)
    count = 0

    for message in messages:
        if cfg.contains(message):
            count += 1

    print('Part 2: Solution {}'.format(count))


part1('input.txt')
part2('input.txt')
