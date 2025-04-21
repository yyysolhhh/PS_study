faces = ["0145", "0123", "0246", "1357", "2367", "4567"]
T = int(input())
for _ in range(T):
    point = "".join(sorted(input().split()))
    if point in faces:
        print("YES")
    else:
        print("NO")