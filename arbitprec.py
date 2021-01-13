from decimal import *

def f(x, s):
    return eval(s)

s = input()
D = int(input())
if D > 20:
    getcontext().prec = D + 10
    delta = Decimal('0.1') ** (D)
else:
    getcontext().prec = D + 10
    delta = Decimal('0.1') ** (D)


a = Decimal('-1.5') + delta
b = Decimal('1.5') - delta
while abs(f(b, s)) > delta:
    if f(b, s) - f(a, s) == 0: break
    #if Decimal('-1.5') < b < Decimal('1.5'):
    b, a = b - (b - a) * f(b, s) / (f(b, s) - f(a, s)), b
    #else:
    #  b = b - (b - a) * f(b, s) / (f(b, s) - f(a, s))
    #t = t - (t - q) * f(t, s) / (f(t, s) - f(q, s))
    #b = a - f(a, s) / (f(a, s) - f(b, s))
    #print(a, b)


#print(b, t)

if not (Decimal('-1.5') < b < Decimal('1.5')):
    a = Decimal('-1.5') + delta
    b = Decimal('1.5') - delta
    while abs(f(b, s)) > delta:
        if f(b, s) - f(a, s) == 0: break
        b = b - (b - a) * f(b, s) / (f(b, s) - f(a, s))


if b == 0:
    print("0."+"0"*D)
else:
    ds = "1." + "0"*D
    print(b.quantize(Decimal(ds)))