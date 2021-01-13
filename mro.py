from re import *
from collections import deque
from time import time

#t = time()
s = input()
classes = list()
linerl = dict()
ret = True
t = time()

while s:
    if ret and len(s) > 5:
        if s[0:5] == "class":
            if "(" in s:
                classes = findall("class (.*)[(].*[)]:", s)
                parents = findall("(?<=[(]).*(?=[)])", s)[0].split(', ')
            else:
                classes = findall("class (.*):", s)
                parents = ['']

            if parents[0] == '':
                linerl[classes[0]] = classes.copy()
            else:
                buf = list()
                buf.append(classes[0])
                #merge_list = list()

                '''
                for p in parents:
                    merge_list.append(linerl[p].copy())
                '''

                merge_list = [linerl[p].copy() for p in parents]

                count_set = set()
                count_set = count_set.union(*merge_list)

                for c in range(len(count_set)):
                    if not ret: break
                    if not any(merge_list): break

                    for m in merge_list:
                        if not len(m): continue
                        b = m[0]

                        for n in range(len(merge_list)):
                            if b in merge_list[n][1:]:
                                ret = False
                                break

                            if len(merge_list[n]) and b == merge_list[n][0]:
                                merge_list[n].pop(0)

                        if ret:
                            buf.append(b)
                        break

                linerl[classes[0]] = buf.copy()
        #print(linerl)
    s = input()
print(time() - t)

if ret:
    print("Yes")
else:
    print("No")