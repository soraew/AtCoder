

N = int(input())
i, x, y = [0, 0, 0]
flag = True

for _ in range(N):
    i_ = i
    y_ = y
    x_ = x
    
    i, x, y = map(int, input().split())
    
    abss = abs(x - x_) + abs(y - y_) 

    absi = abs(i_ - i)

    
    if (abss > absi) or (abss % 2) != (absi % 2):
        flag = not flag
        break
    else:
        pass
    
if not flag:
    print("No")
else:
    print("Yes")