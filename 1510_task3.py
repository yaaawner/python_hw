from sys import *
from random import *

N = int(argv[1])
if len(argv) > 2:
    seed(int(argv[2]))
else:
    seed(100)

A = input().lower()
D = dict()
for i in range(len(A) - 1):
    if A[i:i+2].isalpha():
        D[A[i:i+2]] = D.get(A[i:i+2], 0) + 1

sout = ""
while len(sout) < N:
    sout += choices(D.keys(), D.values(), k = 1)
