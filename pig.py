from re import *
# "aouieAOUIE"

def syl(s):
    count = 0
    for i in "aouieAOUIE":
        if i in s:
            count += s.count(i)
    return count

pattern1 = r'([(]?)([^aouieAOUIE]+)((?:[aouieAOUIE]*[^aouieAOUIE.,-?!)";:]*)+)([.,-?!)";:]*)'
repl1 = r'\1\3\2ay\4'
#s1 = sub(pattern1, repl1, "stupid")
#print(s1)

pattern2 = r'([aouieAOUIE])([^aouieAOUIE]*)((?:[aouieAOUIE]*[^aouieAOUIE.,-?!);:"]*)+)([.,-?!)";:]*)'
repl2 = r'\3\1\2ay\4'
#s2 = sub(pattern2, repl2, 'ages"')
#print(s2)

pattern3 = r'([(]?)([aouieAOUIE][^aouieAOUIE.,-?!)";:]*)([.,-?!)";:]*)'
repl3 = r'\1\2yay\3'
#s3 = sub(pattern3, repl3, "egg")
#print(s3)

#l = split(" ", "This is an example of Hog Latin. As you can see, it's silly,")
#print(l)

#print(syl("egg"))
#a = str()
slatin = input()
while slatin:
    flag = False
    l = slatin.split()
    #print(l)
    l_new = list()
    for i in l:
        flag = flagl = False
        if i[0] == "(":
            i = i[1:]
            flag = True
        if i and i[0] == '"':
            i = i[1:]
            flagl = True
        a = i
        if "-" in i:
            lk = split("-", i)
            a = ""
            for k in lk:
                b = k
                if syl(k):
                    if k[0] in "aouie":
                        if syl(k) == 1:
                            b = sub(pattern3, repl3, k)
                        else:
                            b = sub(pattern2, repl2, k)

                    elif k[0] in "AOUIE":
                        if syl(k) == 1:
                            b = sub(pattern3, repl3, k.lower())
                        else:
                            b = sub(pattern2, repl2, k.lower())
                        b = b[0].upper() + b[1:]

                    elif k[0].islower():
                        b = sub(pattern1, repl1, k)
                    else:
                        b = sub(pattern1, repl1, k.lower())
                        b = b[0].upper() + b[1:]

                a += b + "-"
                #print(a, b)
            a = a[:-1]

        elif "/" in i:
            lk = split("/", i)
            a = ""
            for k in lk:
                b = k
                if syl(k):
                    if k[0] in "aouie":
                        if syl(k) == 1:
                            b = sub(pattern3, repl3, k)
                        else:
                            b = sub(pattern2, repl2, k)

                    elif k[0] in "AOUIE":
                        if syl(k) == 1:
                            b = sub(pattern3, repl3, k.lower())
                        else:
                            b = sub(pattern2, repl2, k.lower())
                        b = b[0].upper() + b[1:]

                    elif k[0].islower():
                        b = sub(pattern1, repl1, k)
                    else:
                        b = sub(pattern1, repl1, k.lower())
                        b = b[0].upper() + b[1:]

                a += b + "/"
                #print(a, b)
            a = a[:-1]

        elif syl(i):
            if i[0] in "aouie":
                if syl(i) == 1:
                    a = sub(pattern3, repl3, i)
                else:
                    a = sub(pattern2, repl2, i)

            elif i[0] in "AOUIE":
                if syl(i) == 1:
                    a = sub(pattern3, repl3, i.lower())
                else:
                    a = sub(pattern2, repl2, i.lower())
                a = a[0].upper() + a[1:]

            elif i[0].islower():
                a = sub(pattern1, repl1, i)
            else:
                a = sub(pattern1, repl1, i.lower())
                a = a[0].upper() + a[1:]
        if flagl:
            a = '"' + a
        if flag:
            a = "(" + a
        l_new.append(a)
        #print(i)

    print(" ".join(l_new))
    l_new.clear()
    slatin = input()