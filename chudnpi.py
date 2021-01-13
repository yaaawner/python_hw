from decimal import *
from math import factorial
#from time import time

getcontext().prec = 10000

def PiGen():
    #getcontext().prec = 10000
    k = 0
    sum = Decimal(0)
    d = Decimal(10005).sqrt() / 4270934400

    while True:
        f = Decimal(factorial(6 * k)) * (Decimal(13591409) + Decimal(545140134) * k)
        t = Decimal(factorial(3 * k)) * Decimal(factorial(k) ** 3) * Decimal(640320 ** (3 * k))
        sum += (Decimal(-1) ** k) * (f / t)
        k += 1
        pi = (sum * d) ** (-1)
        yield pi

#getcontext().prec = 10000
#k = 0
#sum = Decimal(0)

#while k < 1:
#    f = Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k)))
#    t = (Decimal(13591409) + Decimal(545140134) * k) / (640320 ** (3 * k))

#    sum += (Decimal(-1) ** k) * (f * t)
#    k += 1
#    pi = (sum * Decimal(10005).sqrt() / 4270934400) ** (-1)

#    print("-------- iteration --------")
#    print(f)
#    print(t)
#    print(sum)
#    print(pi)


#start_time = time.time()
#sum = Decimal(0)
#d = Decimal(10005).sqrt() / 4270934400
#for k in range(100):
#    f = Decimal(factorial(6 * k)) * (Decimal(13591409) + Decimal(545140134) * k)
#    t = (factorial(3 * k)) * (factorial(k) ** 3) * (640320 ** (3 * k))
#    sum += (Decimal(-1) ** k) * (f / t)
#    pi = (sum * d) ** (-1)
#print("--- %s seconds ---" % (time.time() - start_time))
#print(f)
#print(t)

#start_time = time()

#print("--- %s seconds ---" % (time() - start_time))