from itertools import product
N, nK = map(int, input().split())
K = list(input().split())
max_len = len(str(N))
while True:
    temp = sorted(product(K, repeat=max_len), reverse=True)
    result = []
    for i in temp:
        ans = int("".join(i))
        if ans <= N:
            result.append(ans)
    if len(result) > 0:
        print(max(result))
        break
    max_len -= 1