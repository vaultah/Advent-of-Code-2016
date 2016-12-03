# Day 3: http://adventofcode.com/2016/day/3

inp = [
    (566,  477,  376),
    (575,  488,  365),
    ( 50,   18,  156),
    (558,  673,  498),
    (133,  112,  510),
    (670,  613,   25),
    ( 84,  197,  643),
    (910,  265,  611),
    (894,  252,  545),
    (581,    3,  598),
    ( 98,  742,  574),
    (628,  746,  193),
    (129,  677,  265),
    (187,  445,  169),
    (288,  242,  128),
    (569,  744,  439),
    (685,  748,  471),
    (256,   23,  157),
    (218,  343,  491),
    (777,  905,  633),
    (778,  867,  840),
    (672,  772,  947),
    (500,  763,  420),
    (449,  665,  653),
    ( 23,  558,  858),
    (745,  407,  904),
    (766,  194,  576)
    # 1965 tuples omitted
]


def first(arg):
    return sum(a + b > c and b + c > a and a + c > b
               for a, b, c in arg)


def second(arg):
    return sum(a + b > c and b + c > a and a + c > b
               for col in zip(*arg) for a, b, c in zip(*[iter(col)]*3))


if __name__ == '__main__':
    print('Valid triangles (rows):', first(inp))
    print('Valid triangles (columns):', second(inp))
