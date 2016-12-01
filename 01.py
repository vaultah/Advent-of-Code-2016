# Day 1: http://adventofcode.com/2016/day/1


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
    lst = input('Enter the directions: ').split(', ')
    print('Shortest distance:', shortest_path(lst))
    print('Distance to the first duplicate location:', first_duplicate(lst))
