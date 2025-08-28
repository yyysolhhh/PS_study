t1 = int(input())
for i in range(t1):
    l=[]
    t2 = int(input())
    for x in range(t2):
        l.append(input())
    dap = 0
    for y in range(t2):
        for x in range(t2):
            if x != y:
                a = l[y]+l[x]
                s = 0
                for i in range(0,len(a)//2):
                    if a[i] != a[-i-1]:
                        s = 1
                if s == 0:
                    dap = a
    if dap != 0:
        print(dap)
    else:
        print(0)