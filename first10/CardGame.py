import sys

N = int(input())

A = list(map(int, input().split()))

A_s = sorted(A, reverse=True)


Alice = 0
Bob = 0

alice = True

while len(A_s) >= 1:
    if alice == True:
        Alice += A_s.pop(0)
    else:
        Bob += A_s.pop(0)
    alice = not alice


print(Alice - Bob)