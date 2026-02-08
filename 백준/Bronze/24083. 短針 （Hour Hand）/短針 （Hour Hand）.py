A = int(input())
B = int(input())
ans = (A + B) % 12
print(ans if ans != 0 else 12)