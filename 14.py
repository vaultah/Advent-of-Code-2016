# Day 14: http://adventofcode.com/2016/day/14

from itertools import count
from hashlib import md5
from functools import lru_cache


inp = 'qzyelonm'


@lru_cache(maxsize=None)
def digest(salt, index, rounds=1):
    s = f'{salt}{index}'
    for _ in range(rounds):
        s = md5(s.encode()).hexdigest()
    return s


def generate(salt, rounds=1):
    n = 0
    for x in count():
        dig = digest(salt, x, rounds=rounds)
        chars = next((t for t in zip(dig, dig[1:], dig[2:]) if len({*t}) == 1), None)
        if chars is None:
            continue

        chars = chars[0] * 5
        if any(chars in digest(salt, y, rounds=rounds) for y in range(x + 1, x + 1001)):
            n += 1
            if n == 64:
                yield n, x, dig


if __name__ == '__main__':
    print('Part 1:', next(i for n, i, _ in generate(inp) if n == 64))
    print('Part 2:', next(i for n, i, _ in generate(inp, rounds=2017) if n == 64))
