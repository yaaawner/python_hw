from random import *
G = "АУЕЫОЭЯИЮ"
S = "ЦКНГШЩЗХФВПРЛДЖЧСМТБ"
lout = [i+j for i in G for j in S] + [j+i for i in G for j in S] + [i for i in G]

N = int(input())

sout = ""
while len(sout) < N:
    sout += choice(lout)

print(sout)
