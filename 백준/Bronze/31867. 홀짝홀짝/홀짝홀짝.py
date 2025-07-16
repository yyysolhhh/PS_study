N = int(input())
K = input()
odd, even = 0, 0
for i in K:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print(0)
elif even < odd:
    print(1)
else:
    print(-1)