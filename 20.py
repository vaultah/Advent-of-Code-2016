# Day 20: http://adventofcode.com/2016/day/20

inp = [(5, 8), (0, 2), (4, 7)]


def allowed(blocked, n):
    rng, *blocked = sorted([*r] for r in blocked)
    for cur in blocked:
        if cur[0] > n:
            break
        elif cur[0] > rng[-1] + 1:
            yield from range(rng[-1] + 1, cur[0])
            rng = cur
        else:
            rng[-1] = max(rng[-1], cur[-1])

    yield from range(rng[-1] + 1, n + 1)


if __name__ == '__main__':
    ips = list(allowed(inp, 9))
    print('There are', len(ips), 'allowed IPs:')
    for i, x in enumerate(ips, start=1):
        print(f'{i}) {x}')
