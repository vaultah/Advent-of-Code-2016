# Day 25: http://adventofcode.com/2016/day/25

from collections import Counter
from itertools import count


inp = [
    'cpy a d',
    'cpy 15 c',
    'cpy 170 b',
    'inc d',
    'dec b',
    'jnz b -2',
    'dec c',
    'jnz c -5',
    'cpy d a',
    'jnz 0 0',
    'cpy a b',
    'cpy 0 a',
    'cpy 2 c',
    'jnz b 2',
    'jnz 1 6',
    'dec b',
    'dec c',
    'jnz c -4',
    'inc a',
    'jnz 1 -7',
    'cpy 2 b',
    'jnz c 2',
    'jnz 1 4',
    'dec b',
    'dec c',
    'jnz 1 -4',
    'jnz 0 0',
    'out b',
    'jnz a -19',
    'jnz 1 -21',
]


def f(instructions, **init):
    reg = Counter(**init)
    i = 0

    def to_int(val):
        try:
            return int(val)
        except ValueError:
            return reg[val]

    while i < len(instructions):
        cmd, *args = instructions[i].split()

        if cmd in {'dec', 'inc'}:
            reg[args[0]] += 1 if cmd == 'inc' else -1
        elif cmd == 'cpy':
            reg[args[-1]] = to_int(args[0])
        elif cmd == 'mul':
            reg[args[2]] = to_int(args[0]) * to_int(args[1])
        elif cmd == 'out':
            yield to_int(args[0])
        elif cmd == 'jnz':
            if to_int(args[0]):
                i += to_int(args[-1])
                continue
        else:
            x = i + to_int(args[-1])
            if x < len(instructions):
                cmd, *args = instructions[x].split()

                if len(args) == 1:
                    cmd = 'dec' if cmd == 'inc' else 'inc'
                elif len(args) == 2:
                    cmd = 'cpy' if cmd == 'jnz' else 'jnz'

                instructions[x] = ' '.join([cmd] + args)

        i += 1

    return reg['a']


for i in count():
    if all(x == y for x, y in zip(f(inp.copy(), a=i), (0, 1) * 4)):
        print(i)
        break
