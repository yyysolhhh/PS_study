Time = input().split()
H = int(Time[0])
M = int(Time[1])
if M < 45:
    M += 15
    if H == 0:
        H = 23
    else:
        H-=1
    print(H, M)
elif M >= 45:
    M -= 45
    print (H, M)