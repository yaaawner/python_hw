from itertools import tee

def YinYang(*L):
    L1, L2 = zip(*(tee(i, 2) for i in L))
    for i in L1:
        for t in i:
            if not t%2:
                yield t

    for i in L2:
        for t in i:
            if t%2:
                yield t