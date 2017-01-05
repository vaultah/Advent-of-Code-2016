# Day 19: http://adventofcode.com/2016/day/19

from math import log

inp = 3014603


if __name__ == '__main__':
    print('Part one:', 2 * inp - 2 ** int(log(inp, 2) + 1) + 1)
    i = 3 ** int(log(inp - 1, 3))
    print('Part two:', max(inp - 2 * i, 0) + inp - i)
