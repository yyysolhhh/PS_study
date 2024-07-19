T = int(input())
prime_list = [False, False] + [True for _ in range(10000-2)]
for i in range(int(10000 ** 0.5) + 1):
    if prime_list[i]:
        for j in range(i+i, 10000, i):
            prime_list[j] = False
for _ in range(T):
    n = int(input())
    goldbach = []
    for i in range(n):
        if prime_list[i]:
            if prime_list[n-i]:
                goldbach.append((i, n-i))
    len_gold = len(goldbach)
    if len_gold % 2 == 0:
        print(*goldbach[len_gold//2-1])
    else:
        print(*goldbach[len_gold//2])