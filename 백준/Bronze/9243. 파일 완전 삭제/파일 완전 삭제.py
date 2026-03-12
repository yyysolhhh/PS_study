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
    for i, j in zip(before, after):
        if i != j:
            ans = "failed"
            break
print(f"Deletion {ans}")
