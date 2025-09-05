N = int(input())
s = set()
for i in range(N+1):
    for j in range(N+1 - i):
        for k in range(N+1 - i - j):
            t = N-i-j-k
            n = i + 5*j + 10*k  + 50*t
            s.add(n)
print(len(s))