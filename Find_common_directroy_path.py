from itertools import takewhile


def lcp(*s):
    return ''.join(ch[0] for ch in takewhile(lambda x: min(x) == max(x),
                                             zip(*s)))


d1 = '/home/user1/tmp/coverage/test'
d2 = '/home/user1/tmp/covert/operator'
d3 = '/home/user1/tmp/coven/members'

common = lcp(d1, d2, d3)

if common[-1] == '/':
    print(common)
else:
    common = common[:common.rfind('/')]
    print(common)
