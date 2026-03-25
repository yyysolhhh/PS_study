import sys
input = sys.stdin.readline
N = int(input())
check = True
for _ in range(N):
    univ = input().strip()
    if univ == "yonsei":
        if check:
            ans = "Yonsei Won!"
        else:
            ans = "Yonsei Lost..."
    elif univ == "korea":
        check = False
print(ans)
