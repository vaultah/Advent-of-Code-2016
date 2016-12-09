# Day 9: http://adventofcode.com/2016/day/9

import re


# The actual input was 212 times longer
inp = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

pattern = re.compile(r'\((\d+)x(\d+)\)')


def first(arg):
    pos = 0
    while True:
        match = pattern.search(arg, pos)
        if match is None:
            break
        chars, num = map(int, match.groups())
        start, end = match.start(), match.end()
        arg = arg[:start] + arg[end:end+chars] * num + arg[end+chars:]
        pos = start + chars * num

    return len(arg)


def _counts(arg):
    while True:
        match = pattern.search(arg)
        if match is None:
            yield len(arg)
            return

        chars, num = map(int, match.groups())
        end = match.end()

        yield match.start() + sum(_counts(arg[end:end+chars])) * num

        arg = arg[end+chars:]


def second(arg):
    return sum(_counts(arg))


if __name__ == '__main__':
    print('Version one:', first(inp), 'characters')
    print('Version two:', second(inp), 'characters')
