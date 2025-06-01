d = []
for _ in range(4):
    d.append(int(input()))
if d[0] == d[1] == d[2] == d[3]:
    print("Fish At Constant Depth")
elif d[0] > d[1] > d[2] > d[3]:
    print("Fish Diving")
elif d[0] < d[1] < d[2] < d[3]:
    print("Fish Rising")
else:
    print("No Fish")