# Day 7: http://adventofcode.com/2016/day/7

import re


inp = [
    'rhamaeovmbheijj[hkwbkqzlcscwjkyjulk]ajsxfuemamuqcjccbc',
    'gdlrknrmexvaypu[crqappbbcaplkkzb]vhvkjyadjsryysvj[nbvypeadikilcwg]jwxlimrgakadpxu[dgoanojvdvwfabtt]yqsalmulblolkgsheo',
    'dqpthtgufgzjojuvzvm[eejdhpcqyiydwod]iingwezvcbtowwzc[uzlxaqenhgsebqskn]wcucfmnlarrvdceuxqc[dkwcsxeitcobaylhbvc]klxammurpqgmpsxsr',
    'gmmfbtpprishiujnpdi[wedykxqyntvrkfdzom]uidgvubnregvorgnhm',
    'txxplravpgztjqcw[txgmmtlhmqpmmwp]bmhfgpmafxqwtrpr[inntmjmgqothdzfqgxq]cvtwvembpvdmcvk',
    'gkxjhpayoyrrpcr[mwyoahlkqyhtznyzrm]mvmurvsrgjunjjepn[mkoumuohilpcfgbmsmh]hpwggyvjkusjxcyojyr[wqxyuzbewpjzlyqmkhw]nniczueulxtdsmkniex',
    'vuzyoofrvaanszwndyt[mzcbhmabgnetrpje]tqnygwhmwrbyosbke[gehqzyhlnyufknqmueo]ngendggbjcvazwol',
    'vdnploylmxnipfudw[pbkxlaozhqhlbzz]kpxnzwjhybgcenyw[fpukiqrjraomftt]rosyxtsdltbsmhykxu[wrucjfwuyypmiic]ydnbgvicfnmwzuatudd',
    'lknaffpzamlkufgt[uvdgeatxkofgoyoi]ajtqcsfdarjrddrzo[bxrcozuxifgevmog]rlyfschtnrklzufjzm',
    'kajqeqlafxtmzirn[mkftybdukmghmyoclxd]plvjnikiozkikifpodt[cmufoktkndkhaeqbztz]drjixnnsdxqnrmn[cmzsnhlirtskunngcee]upgxlcjhmoethppx',
    'joibiixuzgtkjquor[xmnqotlqrhpvlglwaxe]kjmfrpihitjydwda',
    'kouyuiijgsmpzynmt[xvwuujrfkqjmtqdh]ukjscwcnwktrfvrmvew[quzbelbcfxknvqc]drtrmvnabjkslahadad',
    'hhlcltfpiwfjhguif[rpasuqltkbudhwjeew]mkcmvbxqukjczex',
    'xxqceycviwyzqxekn[tiidftrsnlgpesxlf]obtbqfgogpwkoqow[dabhpdntfvbhgtmupy]hbvtghnycgyywavqbtg',
    'zlqdqmuxebccmndzbl[ykefimjzdqdmfvlflj]ptlphteflzxmolkof',
    'babzuaikmedruqsuuv[emlhynmvfhsigdryo]iyblsqlpplrlahtwr',
    'byddropvzudnjciymyh[jcebyxyvikkshpn]ggmrxgkzsrfkfkzo'
    # 1983 lines omitted
]


def has_abba(s):
    return any(w[:2] == w[3:1:-1] and w[0] != w[1]
               for w in zip(s, s[1:], s[2:], s[3:]))


def find_abas(s):
    return [w for w in zip(s, s[1:], s[2:]) if w[0] == w[2] != w[1]]


def first(arg):
    count = 0
    for ip in arg:
        sections = re.split(r'(\[.*?])', ip)
        sup, hyp = sections[::2], sections[1::2]
        count += any(map(has_abba, sup)) and not any(map(has_abba, hyp))

    return count


def second(arg):
    count = 0
    for ip in arg:
        sections = re.split(r'(\[.*?])', ip)
        sup, hyp = sections[::2], sections[1::2]
        babs = {b + a + b for x in sup for a, b, a in find_abas(x)}
        count += any(bab in x for bab in babs for x in hyp)

    return count


if __name__ == '__main__':
    print(first(inp), 'IPs support TLS')
    print(second(inp), 'IPs support SSL')
