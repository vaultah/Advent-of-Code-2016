# Day 17: http://adventofcode.com/2016/day/17

from itertools import compress
from collections import deque
from hashlib import md5


inp = 'pvhmgsws'

moves = {
    'U': ( 0, -1),
    'D': ( 0,  1),
    'L': (-1,  0),
    'R': ( 1,  0)
}


def allowed(vertex, dirs):
    chars = md5(f'{inp}{dirs}'.encode()).hexdigest()[:4]
    for dir, (dx, dy) in compress(moves.items(), (c in 'bcdef' for c in chars)):
        nxt = (vertex[0] + dx, vertex[1] + dy)
        if 0 <= nxt[0] <= 3 and 0 <= nxt[1] <= 3:
            yield dir, nxt


def bfs(start, goal):
    queue = deque([(start, '')])
    while queue:
        vertex, dirs = queue.popleft()
        for dir, nxt in allowed(vertex, dirs):
            if nxt == goal:
                yield dirs + dir
            else:
                queue.append((nxt, dirs + dir))


if __name__ == '__main__':
    directions = list(bfs((0, 0), (3, 3)))
    print('The shortest path to vault is', directions[0])
    print('The length of the longest path to vault is', len(directions[-1]))
