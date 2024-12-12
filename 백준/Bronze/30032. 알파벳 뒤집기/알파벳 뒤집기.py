N, D = map(int, input().split())
alpha = {"d": "qb", "b": "pd", "q": "dp", "p": "bq"}
for _ in range(N):
    ex = input()
    ans = ""
    for i in ex:
        ans += alpha[i][D - 1]
    print(ans)