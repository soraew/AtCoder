
import sys

N = int(input())

A = list(map(int, input().split()))
   
count = 0  
while True:
  bools = [A[i]%2!=0 for i in range(N)]
  if any(bools):
  	break
  for i in range(N):
    a = A[i] / 2
    if a < 1:
      break
    else:
      A[i] = a
  count += 1
  
print(count)
