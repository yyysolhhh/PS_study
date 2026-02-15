s = input()
find = 'UCPC'
idx = 0
for i in s:
    if i == find[idx]:
        idx += 1
    if idx == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")