from itertools import *
N = 7
L = list(filter(lambda x: x.count('TOR') == 2, ["".join(i) for i in product("TOR", repeat = N)]))
print(*L)