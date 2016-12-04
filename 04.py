# Day 4: http://adventofcode.com/2016/day/4

import string


inp = [
    'ryexqpqhteki-uww-iqbui-972[whlao]',
    'guahyncw-zfiqyl-mylpcwym-292[hakyd]',
    'mybbycsfo-tovvilokx-wkbuodsxq-640[pwdms]',
    'sehheiylu-sxesebqju-cqdqwucudj-166[dqtmn]',
    'emixwvqhml-ntwemz-bziqvqvo-512[mqvei]',
    'willimcpy-wuhxs-yhachyylcha-136[wmdkg]',
    'aietsrmdih-jpsaiv-wlmttmrk-802[pndyu]',
    'xst-wigvix-veffmx-irkmriivmrk-854[vzbjm]',
    'dpmpsgvm-dboez-dpbujoh-dvtupnfs-tfswjdf-831[nzcoy]',
    'wlqqp-irsszk-rercpjzj-815[bjyfk]',
    'kyelcrga-aylbw-amyrgle-sqcp-rcqrgle-730[engxw]',
    'ghkmaihex-hucxvm-lmhktzx-501[hmxka]'
    # 923 rooms omitted
]


def first(arg):
    i = 0
    for x in arg:
        *name, last = x.split('-')
        id, check = last.split('[')
        s = ''.join(name)
        l = sorted({*s}, key=lambda x: (-s.count(x), x))
        if l[:5] == [*check.strip(']')]:
            i += int(id)

    return i


def second(arg):
    for x in arg:
        *name, last = x.split('-')
        id = int(last.split('[')[0])
        for w in name:
            s = ''.join(string.ascii_lowercase[(ord(c) - ord('a') + id) % 26] for c in w)
            if 'north' in s:
                print(x, s, id)


if __name__ == '__main__':
    print('Sum of sector IDs:', first(inp))
    print('Rooms containing \'north\':')
    second(inp)
