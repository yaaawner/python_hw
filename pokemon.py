Pl = dict()
Ca = dict()
s = input()

while s:
    l = s.split(" / ")
    if not l[0].isdigit():
        Pl[l[0]] = Pl.get(l[0], list())
        Pl[l[0]].append(l[1])
    else:
        Ca[l[0]] = Ca.get(l[0], list())
        Ca[l[0]].append(l[1])
    s = input()

pok = dict()
for i in Pl.keys():
    for j in Pl[i]:
        for w in Ca[j]:
            pok[w] = pok.get(w, 0) + 1
    Pl[i] = len(pok)
    pok.clear()

max = 0
for i in Pl.values():
    if i > max:
        max = i

ret = list()
for i in Pl.keys():
    if Pl[i] == max:
        ret.append(i)

for i in range(len(ret)):
    for j in range(i + 1, len(ret)):
        if ret[i] > ret[j]:
            ret[i], ret[j] = ret[j], ret[i]

for i in ret:
    print(i)