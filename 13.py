# Day 13: http://adventofcode.com/2016/day/13

from collections import deque


inp = 1362


def allowed(x, y):
    p = x**2 + 2*x*y + y**2 + 3*x + y + inp
    return x >= 0 and y >= 0 and not format(p, 'b').count('1') % 2


def bfs(start):
    queue, visited = deque([(start, 0)]), {}
    moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue:
        vertex, depth = queue.popleft()
        visited[vertex] = depth
        for nxt in ((vertex[0] + dx, vertex[1] + dy) for dx, dy in moves):
            if nxt not in visited and allowed(*nxt):
                queue.append((nxt, depth + 1))

    return visited


if __name__ == '__main__':
    visited = bfs((1, 1))
    print('The shortest path to (31, 39) has', visited[31, 39], 'steps')
    print(sum(v <= 50 for v in visited.values()), 'locations are reachable in at most 50 steps')
