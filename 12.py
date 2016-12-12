# Day 12: http://adventofcode.com/2016/day/12


from collections import Counter


inp = [
    'cpy 1 a',
    'cpy 1 b',
    'cpy 26 d',
    'jnz c 2',
    'jnz 1 5',
    'cpy 7 c',
    'inc d',
    'dec c',
    'jnz c -2',
    'cpy a c',
    'inc a',
    'dec b',
    'jnz b -2',
    'cpy c b',
    'dec d',
    'jnz d -6',
    'cpy 17 c',
    'cpy 18 d',
    'inc a',
    'dec d',
    'jnz d -2',
    'dec c',
    'jnz c -5'
]


def f(instructions, **init):
    reg = Counter(**init)

    i = 0

    while i < len(instructions):
        l = instructions[i]
        split = l.split()

        if split[0] in {'dec', 'inc'}:
            reg[split[1]] += 1 if split[0] == 'inc' else -1
        elif split[0] == 'cpy':
            try:
                reg[split[-1]] = int(split[1])
            except ValueError:
                reg[split[-1]] = reg[split[1]]
        else:
            try:
                value = int(split[1])
            except ValueError:
                value = reg[split[1]]

            jump = int(split[-1])

            if value:
                i += jump
                continue

        i += 1

    return reg['a']


if __name__ == '__main__':
    print('The value in register a is', f(inp))
    print('The value in register a after initializing c to 1 is', f(inp, c=1))
