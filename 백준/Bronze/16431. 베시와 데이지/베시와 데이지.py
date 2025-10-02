Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())
b = max(abs(Br - Jr), abs(Bc - Jc))
d = abs(Dr - Jr) + abs(Dc - Jc)
if b < d:
    print("bessie")
elif b > d:
    print("daisy")
else:
    print("tie")