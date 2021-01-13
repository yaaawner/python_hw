#from time import time

code = input().split()
bstr = input()
p = 'ПРОЦ'.encode('koi8-r')
ret = str()

table1 = list()
table1_str = list()
table2 = list()
table2_str = list()
table3 = list()
table3_str = list()

#ti = time()
#print(lal)

for c in code:
    for o in code:
        if c == o: continue
        try:
            buf = p.decode(c).encode(o)
        except:
            pass
        else:
            table1.append((c, o))
            table1_str.append(buf)

for i in range(len(table1_str)):
    try:
        if bstr.find(table1_str[i].hex()) == 0:
            s = bytes.fromhex(bstr).decode(table1[i][1]).encode(table1[i][0]).decode('koi8-r')
            if s[0:4] == 'ПРОЦ' and (s[-5:-1] == 'КНЦ;' or s[-4:] == 'КНЦ;'):
                ret = s
                break
    except:
        pass
#print(table1)

if not ret:
    for i in range(len(table1_str)):
        for c in code:
            if c == table1[i][1]: continue
            for o in code:
                if c == o: continue
                try:
                    buf = table1_str[i].decode(c).encode(o)
                except:
                    pass
                else:
                    table2.append((table1[i][0], table1[i][1], c, o))
                    table2_str.append(buf)

    for i in range(len(table2_str)):
        try:
            if bstr.find(table2_str[i].hex()) == 0:
                s = bytes.fromhex(bstr).decode(table2[i][3]).encode(table2[i][2])\
                    .decode(table2[i][1]).encode(table2[i][0]).decode('koi8-r')
                if s[0:4] == 'ПРОЦ' and (s[-5:-1] == 'КНЦ;' or s[-4:] == 'КНЦ;'):
                    ret = s
                    break
                #print("FIND!")
        except:
            pass

if not ret:
    for i in range(len(table2_str)):
        for c in code:
            if c == table2[i][3]: continue
            for o in code:
                if c == o: continue
                try:
                    buf = table2_str[i].decode(c).encode(o)
                except:
                    pass
                else:
                    table3.append((table2[i][0], table2[i][1], table2[i][2], table2[i][3], c, o))
                    table3_str.append(buf)

    for i in range(len(table3_str)):
        try:
            if bstr.find(table3_str[i].hex()) == 0:
                s = bytes.fromhex(bstr).decode(table3[i][5]).encode(table3[i][4])\
                    .decode(table3[i][3]).encode(table3[i][2]).decode(table3[i][1]).encode(table3[i][0]).decode('koi8-r')
                if s[0:4] == 'ПРОЦ' and (s[-5:-1] == 'КНЦ;' or s[-4:] == 'КНЦ;'):
                    ret = s
                    break
        except:
            pass

#print(4)
if not ret:
    table4 = list()
    table4_str = list()
    #print(len((table3_str)))
    for i in range(len(table3_str)):
        for c in code:
            if c == table3[i][5]: continue
            for o in code:
                if c == o: continue
                try:
                    table4_str.append(table3_str[i].decode(c).encode(o))
                except:
                    pass
                else:
                    table4.append((table3[i][0], table3[i][1], table3[i][2], table3[i][3],
                                   table3[i][4], table3[i][5], c, o))
                    #print(time() - ti)

    for i in range(len(table4_str)):
        try:
            if bstr.find(table4_str[i].hex()) == 0:
                s = bytes.fromhex(bstr).decode(table4[i][7]).encode(table4[i][6]) \
                    .decode(table4[i][5]).encode(table4[i][4]).decode(table4[i][3]).encode(table4[i][2]) \
                    .decode(table4[i][1]).encode(table4[i][0]).decode('koi8-r')

                #print(s)
                if s[0:4] == 'ПРОЦ' and (s[-5:-1] == 'КНЦ;' or s[-4:] == 'КНЦ;'):

                    #print(table4[i])
                    ret = s
                    break
        except:
            pass
#print(table4)
print(ret)

#print(time() - ti)