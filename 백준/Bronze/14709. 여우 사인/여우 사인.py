N = int(input())
fox = [1, 3, 4]
ans = "Wa-pa-pa-pa-pa-pa-pow!"
if N != 3:
    ans = "Woof-meow-tweet-squeek"
for _ in range(N):
    n1, n2 = map(int, input().split())
    if n1 not in fox or n2 not in fox:
        ans = "Woof-meow-tweet-squeek"
print(ans)
