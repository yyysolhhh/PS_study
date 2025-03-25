ans = int(input())
ans -= sum(int(input()) for _ in range(9))
print(ans)