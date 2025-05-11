N = int(input())
for i in range(N, 0, -1):
    print(f"{i} bottle{"s" if i > 1 else ""} of beer on the wall, {i} bottle{"s" if i > 1 else ""} of beer.")
    print(f"Take one down and pass it around, {i - 1 if i > 1 else "no more"} bottle{"s" if i > 2 or i == 1 else ""} of beer on the wall.")
    print()
print(f"No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {N} bottle{"s" if N > 1 else ""} of beer on the wall.")