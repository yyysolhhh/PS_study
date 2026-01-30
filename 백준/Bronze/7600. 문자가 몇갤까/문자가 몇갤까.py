import sys
input = sys.stdin.readline
while True:
    sen = input().strip()
    if sen == "#":
        break
    sen = sen.lower().replace(" ", "")
    alpha = set(i for i in sen if i.isalpha())
    print(len(alpha))