N = int(input())
M = int(input())
S = input()
IOI = 0
PN = 0
i = 1
while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        IOI += 1
        if IOI == N:
            PN += 1
            IOI -= 1
        i += 1
    else:
        IOI = 0
    i += 1
print(PN)