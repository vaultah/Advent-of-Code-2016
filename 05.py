# Day 5: http://adventofcode.com/2016/day/5

from itertools import count
from hashlib import md5


inp = 'cxdnnyjw'


def first(arg):
    pwd = ''

    for i in count():
        dig = md5(f"{arg}{i}".encode()).hexdigest()
        if dig.startswith('00000'):
            pwd += dig[5]
            if len(pwd) == 8:
                return pwd


def second(arg):
    pwd = {}

    for i in count():
        dig = md5(f"{arg}{i}".encode()).hexdigest()
        if dig.startswith('00000'):
            if dig[5] not in {'0', '1', '2', '3', '4', '5', '6', '7'}:
                continue

            x = int(dig[5])

            if x in pwd:
                continue

            pwd[x] = dig[6]

            if len(pwd) == 8:
                return ''.join([v for k, v in sorted(pwd.items())])


if __name__ == '__main__':
    print('First password:', first(inp))
    print('Second password:', second(inp))
