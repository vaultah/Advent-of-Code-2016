# Day 21: http://adventofcode.com/2016/day/21

from itertools import permutations


inp = [
    'swap position 2 with position 7',
    'swap letter f with letter a',
    'swap letter c with letter a',
    'rotate based on position of letter g',
    'rotate based on position of letter f',
    'rotate based on position of letter b',
    'swap position 3 with position 6',
    'swap letter e with letter c',
    'swap letter f with letter h',
    'rotate based on position of letter e',
    'swap letter c with letter b',
    'rotate right 6 steps',
    'reverse positions 4 through 7',
    'rotate based on position of letter f',
    'swap position 1 with position 5',
    'rotate left 1 step',
    'swap letter d with letter e',
    'rotate right 7 steps',
    # Some lines omitted
]


def scramble(string, instructions):
    for i in instructions:
        sp = i.split()
        ints = [int(x) for x in sp if x.isdigit()]
        if i.startswith('swap p'):
            temp = list(string)
            temp[ints[1]], temp[ints[0]] = temp[ints[0]], temp[ints[1]]
            string = ''.join(temp)
        elif i.startswith('swap l'):
            string = string.translate(str.maketrans(sp[2] + sp[-1], sp[-1] + sp[2]))
        elif i.startswith('reverse'):
            x, y = ints
            string = string[:x] + string[x:y+1][::-1] + string[y+1:]
        elif i.startswith('move'):
            temp = list(string)
            temp.insert(ints[-1], temp.pop(ints[0]))
            string = ''.join(temp)
        elif i.startswith('rotate b'):
            pos = string.index(i[-1])
            rot = (1 + pos + (pos >= 4)) % len(string)
            string = string[-rot:] + string[:-rot]
        else:
            # left/right
            x = ints[0]
            if sp[1] != 'left':
                x *= -1
            string = string[x:] + string[:x]

    return string


def unscramble(string, instructions):
    for p in permutations(string):
        x = ''.join(p)
        if scramble(x, instructions) == string:
            return x


if __name__ == '__main__':
    print('The result of scrambling \'abcdefgh\' is', repr(scramble('abcdefgh', inp)))
    print('The result of un-scrambling \'fbgdceah\' is', repr(unscramble('fbgdceah', inp)))
