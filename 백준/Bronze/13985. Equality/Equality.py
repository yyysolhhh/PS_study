line = input()
a, b, c = map(int, (line[0], line[4], line[8]))
print("YES" if a + b == c else "NO")