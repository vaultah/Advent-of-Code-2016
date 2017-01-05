# Day 6: http://adventofcode.com/2016/day/6

from collections import Counter


inp = [
    'zbpyuuwm',
    'kobzhfjl',
    'ixzhdvlt',
    'kaocobts',
    'zvibydrv',
    'apmgptcz',
    'xwlmhenu',
    'kxejeclq',
    'hxoouxor',
    'rlytjgev',
    'qaftppcw',
    'sozxfiaf',
    'sudsdedx',
    'dfkcuabm',
    'qztpvgtk',
    'bkifclzk',
    'esoukwnn',
    'zrhtjxfe',
    'oqgzifhj'
    # 553 lines omitted
]


def first(arg):
    return ''.join(Counter(c).most_common(1)[0][0] for c in zip(*arg))


def second(arg):
    return ''.join(Counter(c).most_common()[-1][0] for c in zip(*arg))


if __name__ == '__main__':
    print(first(inp))
    print(second(inp))
