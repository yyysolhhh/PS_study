og = 120 - (9 * 1 + 4 * 3 + 8 * 1)
for i in range(1, 4):
    og += int(input()) * (2 + (-1) ** i)
print(f"The 1-3-sum is {og}")