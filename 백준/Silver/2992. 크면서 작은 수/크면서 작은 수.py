from itertools import permutations
n = input()
perm = sorted(list(permutations(n,len(n))))

for i in perm:
  if n < ''.join(i):
    print(''.join(i))
    break
else:
  print(0)