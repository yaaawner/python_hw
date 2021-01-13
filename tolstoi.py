from operator import itemgetter

N, W = eval(input())
D = {}
s = input().lower()
seps = ''',.;':!"?-'''

while s:
    for d in seps:
        s = s.replace(d,' ')
    for w in s.split():
        if w.isalpha():
            D[w] = D.get(w, 0) + 1
    s = input().lower()

lit = [(u, v) for u, v in D.items() if len(u) >= W]
lit = sorted(lit, key=itemgetter(1), reverse=True)

ret = list()
count = 0
for i in range(len(lit)):
    if i > 0 and lit[i][1] != lit[i-1][1]:
        count += 1
    if N == count:
        break
    ret.append(lit[i])

for i in range(len(ret)):
    for j in range(i + 1, len(ret)):
        if ret[i][1] > ret[j][1]:
            ret[i], ret[j] = ret[j], ret[i]

for i in range(len(ret)):
    for j in range(i + 1, len(ret)):
        if ret[i][1] == ret[j][1]:
            if ret[i][0] > ret[j][0]:
                ret[i], ret[j] = ret[j], ret[i]

for u, v in ret:
    print('{}: {}'.format(v, u))