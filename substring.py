from collections import UserString
#from collections import Counter
#print(dir(str))

class SubString(UserString):
    def __sub__(self, other):
        from collections import Counter
        o = Counter(other)
        l = list()
        for i in self:
            if type(other)(i) in other and o[i] > 0:
                o[i] -= 1
            else:
                l.append(str(i))
        #print(l)
        #ret = "".join(l)
        #del (Counter)
        return type(self)("".join(l))

del(UserString)
#print(SubString("qwertyerty")-SubString("ttttr"))
#del(Counter, UserString)
#print(dir())

#import string
#S=SubString("NOTE: gravity is a myth, the Earth sucks.")
#print(S-string.ascii_lowercase)
#print(string.digits+S-string.ascii_uppercase)
