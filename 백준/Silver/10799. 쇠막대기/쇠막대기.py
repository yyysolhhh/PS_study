import sys
bra = sys.stdin.readline().strip()
stick = []
result = 0
for i in range(len(bra)):
    if bra[i] == '(':
        stick.append(1)
    else:
        if bra[i-1] == '(':
            stick.pop()
            result += len(stick)
        else:
            stick.pop()
            result += 1
print(result)