import sys
input = sys.stdin.readline
MAX = 119
prime = [False, False] + [True for _ in range(2, MAX)]
for i in range(2, MAX):
    for j in range(i * 2, MAX, i):
        if prime[j]:
            prime[j] = False
N = int(input())
for _ in range(N):
    ans = "No"
    a = int(input())
    for i in range(2, a):
        if prime[i] and prime[a - i]:
            ans = "Yes"
            break
    print(ans)