# Day 10: http://adventofcode.com/2016/day/10

from collections import defaultdict


inp = [
    'bot 88 gives low to bot 51 and high to bot 42',
    'bot 13 gives low to bot 4 and high to bot 167',
    'bot 90 gives low to bot 78 and high to bot 199',
    'bot 84 gives low to bot 205 and high to bot 201',
    'bot 41 gives low to bot 48 and high to bot 15',
    'bot 15 gives low to bot 156 and high to bot 54',
    'bot 70 gives low to output 10 and high to bot 4',
    'bot 140 gives low to bot 206 and high to bot 189',
    'value 67 goes to bot 187',
    # 222 lines omitted
]


def factory(arg):
    prod = 1
    bots, instructions = defaultdict(list), {}

    for l in arg:
        split = [int(x) if x.isdigit() else x for x in l.split()]
        if l.startswith('value'):
            bots[split[-1]] += split[1],
        else:
            instructions[split[1]] = (split[5], split[6], split[-2], split[-1])

    while True:
        id = next((k for k, v in bots.items() if len(v) > 1), None)
        if id is None:
            break

        low, lid, high, hid = instructions[id]
        m, M = sorted(bots.pop(id))

        if (m, M) == (17, 61):
            print('Bot', id, 'is responsible for comparing 61 and 17')

        if low == 'bot':
            bots[lid] += m,
        else:
            if lid in {0, 1, 2}:
                prod *= m

        if high == 'bot':
            bots[hid] += M,
        else:
            if hid in {0, 1, 2}:
                prod *= M

    print('Product of values in outputs 0, 1, 2 is', prod)


if __name__ == '__main__':
    factory(inp)
