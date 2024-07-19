import sys
input = sys.stdin.readline
A, B = map(int, input().split())
underprime = 0
prime_list = [False, False] + [True for _ in range(2, B+1)]
n_factor = [0 for _ in range(B+1)]
for i in range(2, B+1):
    if prime_list[i]:
        for j in range(i+i, B+1, i):
            prime_list[j] = False
            temp = j
            while temp % i == 0:
                temp //= i
                n_factor[j] += 1
for i in range(A, B+1):
    if prime_list[n_factor[i]]:
        underprime += 1
print(underprime)