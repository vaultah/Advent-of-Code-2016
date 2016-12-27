# Day 23: http://adventofcode.com/2016/day/23

from collections import Counter


inp = [
    'cpy a b',
    'dec b',
    'cpy a d',
    'cpy 0 a',
    # Optimized instructions
    'mul b d a',
    'jnz 0 0',
    'jnz 0 0',
    'jnz 0 0',
    'jnz 0 0',
    'jnz 0 0',
    # ---
    'dec b',
    'cpy b c',
    'cpy c d',
    'dec d',
    'inc c',
    'jnz d -2',
    'tgl c',
    'cpy -16 c',
    'jnz 1 c',
    'cpy 94 c',
    'jnz 99 d',
    'inc a',
    'inc d',
    'jnz d -2',
    'inc c',
    'jnz c -5'
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


if __name__ == '__main__':
    print('The value in register a after initializing a to 7 is', f(inp.copy(), a=7))
    print('The value in register a after initializing a to 12 is', f(inp.copy(), a=12))
