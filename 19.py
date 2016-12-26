# Day 19: http://adventofcode.com/2016/day/19

from math import log

n = 3014603


if __name__ == '__main__':
    print('Part one:', 2 * n - 2 ** int(log(n, 2) + 1) + 1)
    i = 3 ** int(log(n - 1, 3))
    print('Part two:', max(n - 2 * i, 0) + n - i)
