import sys
from itertools import combinations
input = sys.stdin.readline
L, C = map(int, input().split())
letters = sorted(input().split())
code = list(combinations(letters, L))
vowel = ['a', 'e', 'i', 'o', 'u']
result = []
for i in code:
    n_vowel = 0
    n_consonant = 0
    for j in i:
        if j in vowel:
            n_vowel += 1
        else:
            n_consonant += 1
    if n_vowel >= 1 and n_consonant >= 2:
        result.append(i)
for i in result:
    print(''.join(i))