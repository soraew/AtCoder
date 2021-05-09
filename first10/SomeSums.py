import sys

N, A, B = map(int, input().split())

def sum(i):
    I = str(i)
    sum = 0
    for j in range(len(I)):
        sum += int(I[j])
    return sum


        
sums = 0
for i in range(1,N+1):
    s = sum(i)
    if A <= s <= B:
        sums += i
    else:
        pass
    
print(sums)