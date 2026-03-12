N = int(input())
before = input()
after = input()
ans = "succeeded"
if N & 1:
    for i, j in zip(before, after):
        if i == j:
            ans = "failed"
            break
else:
    if before != after:
        ans = "failed"
print(f"Deletion {ans}")
