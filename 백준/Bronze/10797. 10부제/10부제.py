n = int(input())
car = list(map(int, input().split()))
ans = sum([True if i % 10 == n else False for i in car])
print(ans)