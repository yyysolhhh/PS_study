N = int(input())
resp = []
for _ in range(N):
    resp.append(input())
cnt = 0
for i in range(N):
    answ = input()
    if resp[i] == answ:
        cnt += 1
print(cnt)