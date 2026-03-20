import sys
input = sys.stdin.readline
N = int(input())
file = []
password = ""
for _ in range(N):
    word = input().strip()
    if word == word[::-1]:
        password = word
    elif word[::-1] in file:
        password = word
    file.append(word)
l = len(password)
print(l, password[l // 2])
