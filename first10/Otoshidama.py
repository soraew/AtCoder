
N, Y = map(int, input().split())




def otoshi(N, Y):
    flag = False
    for ten in range(N+1):
        for fiv in range(N - ten +1):
            one = N - ten - fiv
            if ten*10000 + fiv*5000 + one*1000 == Y:
                print("{} {} {}".format(ten, fiv, one))
                flag = not flag
                return 0
            else:
                pass
    if not flag:
        print("-1 -1 -1")
        
otoshi(N, Y)