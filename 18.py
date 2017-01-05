# Day 18: http://adventofcode.com/2016/day/18

inp = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'


def safe(start, n):
    prev, count = start, start.count('.')
    for _ in range(n - 1):
        padded = f'.{prev}.'
        prev = ''.join('.^'[l != r] for l, c, r in zip(padded, padded[1:], padded[2:]))
        count += prev.count('.')

    return count


if __name__ == '__main__':
    print('The number of safe tiles in the first 40 rows is', safe(inp, 40))
    print('The number of safe tiles in the first 400000 rows is', safe(inp, 400000))
