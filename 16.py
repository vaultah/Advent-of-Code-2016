# Day 16: http://adventofcode.com/2016/day/16


inp = '11101000110010100'


def checksum(initial, length):
    table = str.maketrans('01', '10')
    data = initial

    while len(data) < length:
        new = data[::-1].translate(table)
        data = f'{data}0{new}'

    check = data[:length]

    while not len(check) % 2:
        check = [int(x == y) for x, y in zip(*[iter(check)]*2)]

    return ''.join(map(str, check))


if __name__ == '__main__':
    print('Checksum for the first disk:', checksum(inp, 272))
    print('Checksum for the second disk:', checksum(inp, 35651584))
