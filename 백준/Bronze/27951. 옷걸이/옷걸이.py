import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
U, D = map(int, input().split())

result = []
possible = True

for i in A:
    if i == 1:
        if U > 0:
            U -= 1
            result.append('U')
        else:
            possible = False
            break
    elif i == 2:
        if D > 0:
            D -= 1
            result.append('D')
        else:
            possible = False
            break
    else:
        if U > 0:
            U -= 1
            result.append('U')
        elif D > 0:
            D -= 1
            result.append('D')
        else:
            possible = False
            break

if possible:
    print("YES")
    print(''.join(result))
else:
    print("NO")