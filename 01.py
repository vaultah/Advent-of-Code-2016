# Day 1: http://adventofcode.com/2016/day/1

inp = [
    'R4', 'R3', 'L3', 'L2', 'L1', 'R1', 'L1', 'R2', 'R3', 'L5', 'L5', 'R4', 'L4', 'R2', 'R4', 'L3', 'R3', 'L3', 'R3', 'R4', 'R2', 'L1',
    'R2', 'L3', 'L2', 'L1', 'R3', 'R5', 'L1', 'L4', 'R2', 'L4', 'R3', 'R1', 'R2', 'L5', 'R2', 'L189', 'R5', 'L5', 'R52', 'R3', 'L1', 'R4',
    'R5', 'R1', 'R4', 'L1', 'L3', 'R2', 'L2', 'L3', 'R4', 'R3', 'L2', 'L5', 'R4', 'R5', 'L2', 'R2', 'L1', 'L3', 'R3', 'L4', 'R4', 'R5', 'L1',
    'L1', 'R3', 'L5', 'L2', 'R76', 'R2', 'R2', 'L1', 'L3', 'R189', 'L3', 'L4', 'L1', 'L3', 'R5', 'R4', 'L1', 'R1', 'L1', 'L1', 'R2', 'L4',
    'R2', 'L5', 'L5', 'L5', 'R2', 'L4', 'L5', 'R4', 'R4', 'R5', 'L5', 'R3', 'L1', 'L3', 'L1', 'L1', 'L3', 'L4', 'R5', 'L3', 'R5', 'R3', 'R3',
    'L5', 'L5', 'R3', 'R4', 'L3', 'R3', 'R1', 'R3', 'R2', 'R2', 'L1', 'R1', 'L3', 'L3', 'L3', 'L1', 'R2', 'L1', 'R4', 'R4', 'L1', 'L1', 'R3',
    'R3', 'R4', 'R1', 'L5', 'L2', 'R2', 'R3', 'R2', 'L3', 'R4', 'L5', 'R1', 'R4', 'R5', 'R4', 'L4', 'R1', 'L3', 'R1', 'R3', 'L2', 'L3', 'R1',
    'L2', 'R3', 'L3', 'L1', 'L3', 'R4', 'L4', 'L5', 'R3', 'R5', 'R4', 'R1', 'L2', 'R3', 'R5', 'L5', 'L4', 'L1', 'L1'
]


def shortest_path(lst):
    facex, facey = 0, 1
    x, y = 0, 0
    for v in lst:
        vd, vn = v[0], int(v[1:])
        facex, facey = (facey, -facex) if vd == 'R' else (-facey, facex)
        x += facex * vn
        y += facey * vn

    return abs(x) + abs(y)


def first_duplicate(lst):
    facex, facey = 0, 1
    x, y = 0, 0
    locations = {(x, y)}

    for v in lst:
        vd, vn = v[0], int(v[1:])
        facex, facey = (facey, -facex) if vd == 'R' else (-facey, facex)

        for _ in range(vn):
            x += facex
            y += facey
            if (x, y) not in locations:
                locations.add((x, y))
            else:
                return abs(x) + abs(y)

    return abs(x) + abs(y)


if __name__ == '__main__':
    print('Shortest distance:', shortest_path(inp))
    print('Distance to the first duplicate location:', first_duplicate(inp))
