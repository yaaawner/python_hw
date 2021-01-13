st = input()
first = list()
second = list()
third = list()
time_first, time_second, time_third = -1, -1, -1

while st:
    h, m, s = st[st.rfind(" "):].split(":")
    h, m, s = int(h), int(m), int(s)
    time_buf = h * 10000 + m * 100 + s

    if time_buf < time_first and time_first >= 0:
        time_third = time_second
        time_second = time_first
        time_first = time_buf

        third = second.copy()
        second = first.copy()
        first.clear()
        first.append(st)

    elif time_first < 0:
        first.append(st)
        time_first = time_buf

    elif time_buf == time_first:
        first.append(st)

    else:
        if time_buf < time_second and time_second >= 0:
            time_third = time_second
            time_second = time_buf

            third = second.copy()
            second.clear()
            second.append(st)

        elif time_second < 0:
            second.append(st)
            time_second = time_buf

        elif time_buf == time_second:
            second.append(st)

        else:
            if time_buf < time_third and time_third >= 0:
                time_third = time_buf
                third.clear()
                third.append(st)

            elif time_third < 0:
                third.append(st)
                time_third = time_buf

            elif time_buf == time_third:
                third.append(st)

    st = input()

max = [0, 0, 0, 0]
lout = list()
buf = list()
first_out = list()
second_out = list()
third_out = list()

for l in first:
    for q in l.split(" ", 2):
        buf.append(q)
    for i in range(2):
        lout.append(buf[i])
    for q in buf[-1].rsplit(" ", 1):
        lout.append(q)

    for i in range(4):
        if len(lout[i]) > max[i]:
            max[i] = len(lout[i])

    first_out.append(lout.copy())
    lout.clear()
    buf.clear()

for l in second:
    for q in l.split(" ", 2):
        buf.append(q)
    for i in range(2):
        lout.append(buf[i])
    for q in buf[-1].rsplit(" ", 1):
        lout.append(q)

    for i in range(4):
        if len(lout[i]) > max[i]:
            max[i] = len(lout[i])

    #print(lout)
    second_out.append(lout.copy())
    lout.clear()
    buf.clear()

for l in third:
    for q in l.split(" ", 2):
        buf.append(q)
    for i in range(2):
        lout.append(buf[i])
    for q in buf[-1].rsplit(" ", 1):
        lout.append(q)

    for i in range(4):
        if len(lout[i]) > max[i]:
            max[i] = len(lout[i])

    third_out.append(lout.copy())
    lout.clear()
    buf.clear()

for i in range(len(first_out)):
    for j in range(i + 1, len(first_out)):
        if first_out[i][1] > first_out[j][1]:
            first_out[i], first_out[j] = first_out[j], first_out[i]
        elif first_out[i][1] == first_out[j][1]:
            if first_out[i][0] > first_out[j][0]:
                first_out[i], first_out[j] = first_out[j], first_out[i]
            elif first_out[i][0] == first_out[j][0] and first_out[i][2] > first_out[j][2]:
                first_out[i], first_out[j] = first_out[j], first_out[i]

for i in range(len(second_out)):
    for j in range(i + 1, len(second_out)):
        if second_out[i][1] > second_out[j][1]:
            second_out[i], second_out[j] = second_out[j], second_out[i]
        elif second_out[i][1] == second_out[j][1]:
            if second_out[i][0] > second_out[j][0]:
                second_out[i], second_out[j] = second_out[j], second_out[i]
            elif second_out[i][0] == second_out[j][0] and second_out[i][2] > second_out[j][2]:
                second_out[i], second_out[j] = second_out[j], second_out[i]

for i in range(len(third_out)):
    for j in range(i + 1, len(third_out)):
        if third_out[i][1] > third_out[j][1]:
            third_out[i], third_out[j] = third_out[j], third_out[i]
        elif third_out[i][1] == third_out[j][1]:
            if third_out[i][0] > third_out[j][0]:
                third_out[i], third_out[j] = third_out[j], third_out[i]
            elif third_out[i][0] == third_out[j][0] and third_out[i][2] > third_out[j][2]:
                third_out[i], third_out[j] = third_out[j], third_out[i]

for l in first_out:
    print("{:<{m1}} {:<{m2}} {:<{m3}} {:<{m4}}".format(l[0], l[1], l[2], l[3],
                                                       m1=max[0], m2=max[1], m3=max[2], m4=max[3]))

for l in second_out:
    print("{:<{m1}} {:<{m2}} {:<{m3}} {:<{m4}}".format(l[0], l[1], l[2], l[3],
                                                       m1=max[0], m2=max[1], m3=max[2], m4=max[3]))

for l in third_out:
    print("{:<{m1}} {:<{m2}} {:<{m3}} {:<{m4}}".format(l[0], l[1], l[2], l[3],
                                                       m1=max[0], m2=max[1], m3=max[2], m4=max[3]))