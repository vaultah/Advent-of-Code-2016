# Day 24: http://adventofcode.com/2016/day/24

from itertools import permutations, combinations
from collections import deque


inp = [
    '###########',
    '#0.1.....2#',
    '#.#######.#',
    '#4.......3#',
    '###########'
]


def bfs(start, end):
    queue = deque([(start, 0)])
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = {start}

    while queue:
        vertex, path = queue.popleft()
        if vertex == end:
            return path

        for nxt in ((vertex[0] + i, vertex[1] + j) for i, j in moves):
            if nxt[0] < 0 or nxt[1] < 0 or nxt[0] >= len(inp) or nxt[1] >= len(inp[0]):
                continue

            if inp[nxt[0]][nxt[1]] != '#' and nxt not in visited:
                queue.append((nxt, path + 1))
                visited.add(nxt)


if __name__ == '__main__':
    paths = {}
    nums = {int(x): (i, j) for i, y in enumerate(inp)
                              for j, x in enumerate(y) if x.isdigit()}

    for a, b in combinations(sorted(nums), 2):
        paths[a, b] = paths[b, a] = bfs(nums[a], nums[b])

    perm = list(permutations(range(1, len(nums))))
    print('Part one:', min(sum(paths[x] for x in zip((0,) + p, p)) for p in perm), 'steps')
    print('Part two:', min(sum(paths[x] for x in zip((0,) + p, p + (0,))) for p in perm), 'steps')
