t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())
maax = t1 * 3 + e1 * 20 + f1 * 120
mel = t2 * 3 + e2 * 20 + f2 * 120
if maax > mel:
    print("Max")
elif maax < mel:
    print("Mel")
else:
    print("Draw")