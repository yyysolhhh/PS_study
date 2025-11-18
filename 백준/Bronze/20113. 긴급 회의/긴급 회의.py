N = int(input())

vote = list(map(int, input().split()))

cnt = [0] * N

 

for i in vote :

    if i == 0 :

        continue

    else :

        cnt[i-1] += 1

 

if cnt.count(max(cnt)) >= 2 or max(cnt) == 0 :

    print('skipped')

else :

    print(cnt.index(max(cnt)) + 1)