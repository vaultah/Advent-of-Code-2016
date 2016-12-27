# Day 22: http://adventofcode.com/2016/day/22

from itertools import permutations
import re


inp = [
    ('/dev/grid/node-x0-y0', 10, 8, 2, 80),
    ('/dev/grid/node-x0-y1', 11, 6, 5, 54),
    ('/dev/grid/node-x0-y2', 32, 28, 4, 87),
    ('/dev/grid/node-x1-y0', 9, 7, 2, 77),
    ('/dev/grid/node-x1-y1', 8, 0, 8, 0),
    ('/dev/grid/node-x1-y2', 11, 7, 4, 63),
    ('/dev/grid/node-x2-y0', 10, 6, 4, 60),
    ('/dev/grid/node-x2-y1', 9, 8, 1, 88),
    ('/dev/grid/node-x2-y2', 9, 6, 3, 66)
]

inp = {(*map(int, re.findall(r'\d+', n)),): s for n, *s in inp}
viable_count = sum(b[-2] > a[1] != 0 for a, b in permutations(inp.values(), 2))
print('The number of viable pairs is', viable_count) 

print('Grid:')

mx, my = max(inp)

for y in range(my + 1):
    for x in range(mx + 1):
        if (x, y) == (0, 0):
            c = '+'
        elif (x, y) == (mx, 0):
            c = 'G'
        elif inp[x, y][0] > 15:
            # find sufficiently large nodes in this input
            c = '#'
        elif not inp[x, y][-1]:
            c = ' '
        else:
            c = '.'

        print(c, end=' ')

    print()
