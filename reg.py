from re import *
reg = input()
names = findall("(?<=<).+?(?=>)", reg)

s = input()
while s:
    a = search(reg, s)
    #print(a)
    if a:
        print("{}: {}".format(a.start(), a.group()))
        i = 1
        for b in a.groups():
            if b:
                if a.start(i) >= 0:
                    print("{}/{}: {}".format(i, a.start(i), b))
            i += 1

        #print(names)
        for n in names:
            if a.group(n):
                if a.start(n) >= 0:
                    print("{}/{}: {}".format(n, a.start(n), a.group(n)))
    else:
        print("<NONE>")

    s = input()