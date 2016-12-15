# Day 15: http://adventofcode.com/2016/day/15

from itertools import count


inp = [(13, 10), (17, 15), (19, 17), (7, 1), (5, 0), (3, 1), (11, 0)]


def sculpture(arg):
    for start in count(1):
        if any((pos + time + start) % n for time, (n, pos) in enumerate(arg, start=1)):
            continue

        return start


if __name__ == '__main__':
    print(f'You can press the button at time={sculpture(inp)}')
