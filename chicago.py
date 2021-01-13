from re import *

B = input()
N = input()

reg = r"\d+\. (?:(?:and )?[a-zA-Z. -]+ [a-zA-Z-]+(?: et al.)?,?)+ .+ [(].+, \d\d\d\d[)], \d+(?:–\d+)*\."
a = findall(reg, B)
print(a)

reg_N = r"(?:[a-zA-Z-]+, [a-zA-Z. -]+)(?:,* (?:and )[a-zA-Z. -]+ [a-zA-Z-]+)*\. .+\. .+, \d\d\d\d\."
an = findall(reg_N, N)
print(an)

if len(a) and len(an):
    reg_g = r". (.+) [(](.+, \d\d\d\d)[)], \d+(?:–\d+)*\."
    g = findall(reg_g, B)
    reg_gN = r"(?:[a-zA-Z-]+, [a-zA-Z. -]+)(?:,* (?:and )[a-zA-Z. -]+ [a-zA-Z-]+)*\. (.+)\. (.+, \d\d\d\d)\."
    gN = findall(reg_gN, N)
    print(gN[0])
    print(g[0])
    reg_names = r"\d+\. (?:([a-zA-Z-]+(?: ?. [a-zA-Z-]+.?)*) ([a-zA-Z-]+))(?:,* (?:and )[a-zA-Z. -]+ [a-zA-Z-]+)*(?:  et al.)?, (?:.+) [(](?:.+, \d\d\d\d)[)], \d+(?:–\d+)*\."
    names = findall(reg_names, B)
    reg_namesN = r"(?:([a-zA-Z-]+), ([a-zA-Z. -]+))(?:,* (?:and )[a-zA-Z. -]+ [a-zA-Z-]+)*\. (?:.+)\. (?:.+, \d\d\d\d)\."
    namesN = findall(reg_namesN, N)
    print(names[0])
    print(namesN[0])

    if gN[0] == g[0] and names[0][1] == namesN[0][0]:
        print("True")
    else:
        print("False")

else:
    print("False")