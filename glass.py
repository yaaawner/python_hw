s = input()
width, high = len(s), 0
stars, high_glass = 0, 0
a, b = 0, 0

while s:
    high += 1
    if s.find("#") >= 0:
        high_glass += 1
        if a == 0 and b == 0:
            a = s.find("#")
            b = s.rfind("#")

        for i in range(a, b):
            if s[i] == "*":
                stars += 1
    s = input()

width_glass = b - a + 1
lvl = 0
if stars % width:
    lvl = stars // width + 1
else:
    lvl = stars // width


for i in range(high):
    if i < high - width_glass:
        print("." * width)
    elif (i == high - width_glass) or (lvl == 0 and i == high - 1):
        print("#" * high_glass + "." * (width - high_glass))
    elif i < high - lvl:
        print("#" + "." * (width - 1))
    else:
        print("*" * width)