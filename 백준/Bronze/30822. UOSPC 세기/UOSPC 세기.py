n = int(input())
S = input()
cnt = [S.count(i) for i in "uospc"]
print(min(cnt))