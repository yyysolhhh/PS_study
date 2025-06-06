Q = int(input())
event = [map(int, input().split()) for _ in range(Q)]
cnt = 0
flag = True
for n, x in event:
    if n == 1:
        cnt += x
    elif n == 2:
        if cnt < x:
            flag = False
            break
        cnt -= x
print("See you next month" if flag else "Adios")