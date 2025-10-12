prime = []

def get_prime():
    is_prime = [False, False] + [True for _ in range(N)]
    for i in range(2, N + 1):
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
    for i in range(N + 1):
        if is_prime[i]:
            prime.append(i)

def solve():
    ans, en = 0, 0
    for st in range(len(prime)):
        en = st + 1
        while en < len(prime) and sum(prime[st:en]) < N:
            en += 1
        if sum(prime[st:en]) == N:
            ans += 1
    return ans

N = int(input())
get_prime()
print(solve())