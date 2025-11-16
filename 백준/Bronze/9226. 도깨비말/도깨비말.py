import sys
input = sys.stdin.readline
vowel = ["a", "e", "i", "o", "u"]
while True:
    word = input().strip()
    if word == "#":
        break
    i = 0
    while i < len(word) and word[i] not in vowel:
        i += 1
    ans = word[i:] + word[:i] + "ay"
    print(ans)