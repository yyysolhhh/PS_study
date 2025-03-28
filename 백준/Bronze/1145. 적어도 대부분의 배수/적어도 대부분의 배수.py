def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
def LCM(a, b):
    return (a * b) // GCD(a, b)
num = list(map(int, input().split()))
res = num[0] * num[1] * num[2] * num[3] * num[4]
for i in range(len(num)):
    for j in range(len(num)):
        if i == j:
            continue
        else:
            temp = LCM(num[i], num[j])
            for k in range(len(num)):
                if k == i or k == j:
                    continue
                else:
                    res = min(res, LCM(temp, num[k]))
print(res)