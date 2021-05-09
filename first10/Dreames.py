S = input()


temp = True

        
while temp and len(S)>0:
    if S[-5:] == "dream" or S[-5:] == "erase":

        S = S[:-5]
    elif S[-6:] == "eraser":

        S = S[:-6]
    elif S[-7:] == "dreamer":

        S = S[:-7]
    else:
        temp = False
        
if temp:
    print("YES")
else:
    print("NO")
