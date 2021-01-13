from random import *

def randsquare(A, B):
    x0 = (A[0] + B[0])/2
    y0 = (A[1] + B[1])/2
    dx = A[0] - B[0]
    dy = A[1] - B[1]
    C = (x0 + dy / 2, y0 - dx / 2)
    D = (x0 - dy / 2, y0 + dx / 2)

    #print(A, B, C, D)
    if randint(0,1) == 1:
        r1 = random()
        r2 = random()
        x = (1 - r1**(0.5)) * A[0] + (r1 ** (0.5) * (1 - r2)) * C[0] + (r1**(0.5) * r2) * B[0]
        y = (1 - r1 ** (0.5)) * A[1] + (r1 ** (0.5) * (1 - r2)) * C[1] + (r1 ** (0.5) * r2) * B[1]
    else:
        r1 = random()
        r2 = random()
        x = (1 - r1 ** (0.5)) * B[0] + (r1 ** (0.5) * (1 - r2)) * D[0] + (r1 ** (0.5) * r2) * A[0]
        y = (1 - r1 ** (0.5)) * B[1] + (r1 ** (0.5) * (1 - r2)) * D[1] + (r1 ** (0.5) * r2) * A[1]

    return (x, y)