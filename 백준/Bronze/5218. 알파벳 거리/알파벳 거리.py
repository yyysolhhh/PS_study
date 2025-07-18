T = int(input())
for _ in range(T):
    ans = []
    w1, w2 = input().split()
    for i in range(len(w1)):
        o1, o2 = ord(w1[i]), ord(w2[i])
        if o1 <= o2:
            ans.append(o2 - o1)
        else:
            ans.append(o2 + 26 - o1)
    print(f"Distances: {" ".join(map(str, ans))}")